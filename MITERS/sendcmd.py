# Sends a command over serial with a newline and carriage return
# usage :
# python sendcmd.py <string>
# <string> is the gcode you want to send
# example :
# python sendcmd.py "11"
# python sendcmd.py "G1 X0 Y0 Z200"


import time
import serial
import sys

consolecmd = sys.argv[1]
vplusconsole = serial.Serial(port='/dev/ttyUSB1', baudrate=9600, timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)


# def waitconsoleready() :
    # retval=vplusconsole.read()
    # sys.stdout.write(retval)
    # while not retval=="." and not retval=="?" :
        # retval=vplusconsole.read()
        # sys.stdout.write(retval)
    # retval=vplusconsole.readline()
    # sys.stdout.write("REC : "+retval)

def writeconsolecommand(command) :
    vplusconsole.write(command)
    vplusconsole.write("\r\n")

# writeconsolecommand("DELETE "+sys.argv[2])
writeconsolecommand(consolecmd)

vplusconsole.close()
