-- Richify Master Piece Crosshair Script
-- Credits: Richify | Discord: @r_0x

local Rayfield = loadstring(game:HttpGet("https://sirius.menu/rayfield"))()

-- Disable Rayfield notifications
if Rayfield.Notify then
    Rayfield.Notify = function() end
end

local Window = Rayfield:CreateWindow({
    Name = "Richify Goated Crosshair",
    LoadingTitle = "The Goat Richify",
    LoadingSubtitle = "by Richify | @r_0x",
    ShowText = "Richify Goat",
    Theme = "Serenity",
    ToggleUIKeybind = "Q",
    ConfigurationSaving = {
        Enabled = true
    },
    KeySystem = false
})

local ClientTab = Window:CreateTab("Client")
ClientTab:CreateSection("Crosshair Settings")

-- Defaults
local CrosshairStyle = "Default"
local CrosshairColor = Color3.fromRGB(255, 255, 255)
local CrosshairSize = 12
local CrosshairThickness = 2
local CrosshairOpacity = 1
local RainbowMode = false

local RainbowHue = 0
local CrosshairGUI
local CrosshairFrames = {}
local Running = true

-- Init GUI
local function InitCrosshairGUI()
    if CrosshairGUI then return end
    local pg = game.Players.LocalPlayer:WaitForChild("PlayerGui")
    CrosshairGUI = Instance.new("ScreenGui")
    CrosshairGUI.Name = "CustomCrosshair"
    CrosshairGUI.ResetOnSpawn = false
    CrosshairGUI.IgnoreGuiInset = true
    CrosshairGUI.Parent = pg
end

-- Clear crosshair
local function ClearCrosshair()
    for _, v in ipairs(CrosshairFrames) do
        v:Destroy()
    end
    CrosshairFrames = {}
end

-- Build Crosshair
local function BuildCrosshair()
    ClearCrosshair()
    if CrosshairStyle == "None" then return end

    local function CreateFrame(x, y, rot)
        local frame = Instance.new("Frame")
        frame.AnchorPoint = Vector2.new(0.5, 0.5)
        frame.Position = UDim2.new(0.5, 0, 0.5, 0)
        frame.Size = UDim2.new(0, x, 0, y)
        frame.Rotation = rot or 0
        frame.BackgroundColor3 = CrosshairColor
        frame.BackgroundTransparency = 1 - CrosshairOpacity
        frame.BorderSizePixel = 0
        frame.Parent = CrosshairGUI
        table.insert(CrosshairFrames, frame)
    end

    if CrosshairStyle == "Dot" then
        CreateFrame(CrosshairThickness * 2, CrosshairThickness * 2)
    elseif CrosshairStyle == "Plus" then
        CreateFrame(CrosshairThickness, CrosshairSize)
        CreateFrame(CrosshairSize, CrosshairThickness)
    elseif CrosshairStyle == "X" then
        CreateFrame(CrosshairThickness, CrosshairSize, 45)
        CreateFrame(CrosshairThickness, CrosshairSize, -45)
    else
        CreateFrame(CrosshairThickness, CrosshairSize)
        CreateFrame(CrosshairSize, CrosshairThickness)
    end
end

-- Update loop
task.spawn(function()
    while Running do
        if CrosshairGUI then
            local color = CrosshairColor
            if RainbowMode then
                RainbowHue = (RainbowHue + 0.005) % 1
                color = Color3.fromHSV(RainbowHue, 1, 1)
            end
            for _, frame in ipairs(CrosshairFrames) do
                frame.BackgroundColor3 = color
                frame.BackgroundTransparency = 1 - CrosshairOpacity
            end
        end
        task.wait(0.03)
    end
end)

InitCrosshairGUI()
BuildCrosshair()

ClientTab:CreateSlider({
    Name = "Crosshair Size",
    Range = {2, 50},
    Increment = 1,
    CurrentValue = CrosshairSize,
    Callback = function(v)
        CrosshairSize = v
        BuildCrosshair()
    end
})

ClientTab:CreateSlider({
    Name = "Opacity",
    Range = {0, 1},
    Increment = 0.05,
    CurrentValue = CrosshairOpacity,
    Callback = function(v)
        CrosshairOpacity = v
        BuildCrosshair()
    end
})

ClientTab:CreateToggle({
    Name = "Rainbow",
    CurrentValue = RainbowMode,
    Callback = function(v)
        RainbowMode = v
    end
})

ClientTab:CreateButton({
    Name = "Uninject",
    Callback = function()
        Running = false
        if CrosshairGUI then
            CrosshairGUI:Destroy()
        end
        Rayfield:Destroy()
    end
})

game.Players.LocalPlayer.CharacterAdded:Connect(function()
    task.wait(1)
    InitCrosshairGUI()
    BuildCrosshair()
end)
