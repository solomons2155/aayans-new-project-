input.onButtonPressed(Button.A, function () {
    basic.showArrow(ArrowNames.North)
    basic.showArrow(ArrowNames.East)
    basic.showArrow(ArrowNames.South)
    basic.showArrow(ArrowNames.West)
})
input.onGesture(Gesture.LogoUp, function () {
    basic.showString("Never do that again.")
})
input.onButtonPressed(Button.AB, function () {
    basic.showArrow(ArrowNames.NorthEast)
    basic.showArrow(ArrowNames.SouthEast)
    basic.showArrow(ArrowNames.SouthWest)
    basic.showArrow(ArrowNames.NorthWest)
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.Diamond)
        basic.showIcon(IconNames.SmallDiamond)
    }
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("I think ")
})
input.onGesture(Gesture.LogoDown, function () {
    basic.showString("I told you to not do that.")
})
basic.showLeds(`
    # # . # #
    # # . # #
    . . . . .
    # . . . #
    . # # # .
    `)
basic.showLeds(`
    # # . . .
    # # . . .
    . . . . .
    # . . . #
    . # # # .
    `)
basic.showLeds(`
    . . . # #
    . . . # #
    . . . . .
    # . . . #
    . # # # .
    `)
basic.forever(function () {
    basic.showIcon(IconNames.Chessboard)
    basic.showIcon(IconNames.Target)
    basic.showIcon(IconNames.Diamond)
    basic.showIcon(IconNames.SmallDiamond)
})
