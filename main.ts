makerbit.onIrButton(IrButton.Up, IrButtonAction.Pressed, function () {
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 255)
    while (Tinybit.Ultrasonic_CarV2() == 30) {
        basic.pause(100)
    }
})
makerbit.connectIrReceiver(DigitalPin.P8)
basic.forever(function () {
	
})
