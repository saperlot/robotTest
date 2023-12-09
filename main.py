def on_ir_button_up_pressed():
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 255)
    while Tinybit.Ultrasonic_CarV2() == 30:
        basic.pause(100)
makerbit.on_ir_button(IrButton.UP, IrButtonAction.PRESSED, on_ir_button_up_pressed)

makerbit.connect_ir_receiver(DigitalPin.P8)

def on_forever():
    pass
basic.forever(on_forever)
