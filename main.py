def on_button_pressed_a():
    basic.show_arrow(ArrowNames.NORTH)
    basic.show_arrow(ArrowNames.EAST)
    basic.show_arrow(ArrowNames.SOUTH)
    basic.show_arrow(ArrowNames.WEST)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    basic.show_string("Never do that again.")
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_ab():
    basic.show_arrow(ArrowNames.NORTH_EAST)
    basic.show_arrow(ArrowNames.SOUTH_EAST)
    basic.show_arrow(ArrowNames.SOUTH_WEST)
    basic.show_arrow(ArrowNames.NORTH_WEST)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for index in range(4):
        basic.show_icon(IconNames.DIAMOND)
        basic.show_icon(IconNames.SMALL_DIAMOND)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("I think ")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_leds("""
    # # . # #
    # # . # #
    . . . . .
    # . . . #
    . # # # .
    """)
basic.show_leds("""
    # # . . .
    # # . . .
    . . . . .
    # . . . #
    . # # # .
    """)
basic.show_leds("""
    . . . # #
    . . . # #
    . . . . .
    # . . . #
    . # # # .
    """)

def on_forever():
    basic.show_icon(IconNames.CHESSBOARD)
    basic.show_icon(IconNames.TARGET)
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.SMALL_DIAMOND)
basic.forever(on_forever)
