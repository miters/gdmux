# gdmux

To run a launch the web interface: `gdmux -consolerate 9600 -consoletty "/dev/ttyUSB0" -datarate 9600 -datatty "/dev/ttyUSB1" -http :5000`

Since this will mainly be running on Linux, we just deal with the serial ports as files.
It's up to the user to set them up with the correct parameters (baudrate, stop bits, parity, etc.) using `stty`.
This keeps things nice and simple.

## Getting/Building

You need to install Go. https://github.com/ethereum/go-ethereum/wiki/Installing-Go

You need to install mercurial. `$ sudo apt-get install mercurial meld`

For the Go parts, everything should work with `go get`. Run `go get github.com/MITERS/gdmux/cmd/gdmux` and gdmux will be installed in your Go bin directory.

## Quickstart

To your computer, connect the AWCII RS232 TERM usb first (as /dev/ttyUSB0)
Then connect the RS232 term port from the main processer (as /dev/ttyUSB1)

    $ sudo minicom /dev/ttyUSB0
      D (load from disk D)
      Y (yes, on scribe marks)
    $ python sendvplus.py gcode.pg gcode #make sure you aren't connected to /dev/ttyUSB0 e.g. with minicom
    $ sudo minicom /dev/ttyUSB0
      . disable dry.run
      . enable power
      . do SPEED 10 ALWAYS
      . do READY
      . do DRIVE 2,60,10
      . do DRIVE 3,40,10
      . do DRIVE 5,-10,10
      . do ABOVE

In another terminal:

    $ gdmux -consolerate 9600 -consoletty "/dev/ttyUSB0" -datarate 9600 -datatty "/dev/ttyUSB1" -http :5000

In a browser, open http://localhost:5000 and paste in the code you want to run.

In the /dev/ttyUSB0 terminal, run the gcode program and you should get "READY"

    . exec gcode
      READY

In the browser, hit "run". **A safe starting position should be G1 X0 Y0 Z200**

The arm should immediately execute your commands.

# Debug

If the arm is not responding, make sure that the response to

    $ python sendcmd.py "11"

on /dev/ttyUSB0 is

    READY
    unknown opcode received

Add more "TYPE" commands to the gcode.pg program to print things out to /dev/ttyUSB0
(then reupload with python and exec on the arm)

If anything doesn't seem to work, abort/kill out of V+ program back to "." prompt, ctrl-c out of gdmux, and start again.

You can check if /dev/ttyUSB1 is working:

    $ python sendvplus.py serialtest.v2 serialtest
    $ sudo minicom /dev/ttyUSB0
      . exec serialtest
    $ sudo minicom /dev/ttyUSB1
      A test of MITERS Staubli
      A test of MITERS Staubli
      <...>

Use `abort` to exit out of the program on the Staubli and the USB1 should stop spitting lines.

# Offset from Gcode to Pendant
x +500
y +0
Z -100

This is hardcoded in at the moment -- see gdmux/cmd/gdmux/main.go

## Testing

To test the command and packages, run `go test ./...`.
