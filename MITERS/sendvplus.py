# Uploader for V+ programs
# usage :
# python sendvplus.py <filename> <vplus_program_name>
# <filename> is the local file, i.e. myprogram.v2
# <vplus_program_name> is the name it will be given on the Staubli controller
# once uploaded you can run the program with EXEC <vplus_program_name>

import time
import serial
import sys

f=open(sys.argv[1],"r")
vplusconsole = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)

d=f.readlines()

def waitconsoleready() :
    retval=vplusconsole.read()
    sys.stdout.write(retval)
    while not retval=="." and not retval=="?" :
        retval=vplusconsole.read()
        sys.stdout.write(retval)
    retval=vplusconsole.readline()
    sys.stdout.write("REC : "+retval)

def writeconsolecommand(command) :
    vplusconsole.write(command)
    vplusconsole.write("\r\n")

writeconsolecommand("DELETE "+sys.argv[2])
waitconsoleready();
writeconsolecommand("Y")
waitconsoleready();
writeconsolecommand("EDIT "+sys.argv[2])
waitconsoleready();

for currentline in d:
    print(currentline)
    writeconsolecommand(currentline)
    waitconsoleready();
    time.sleep(0.05)

writeconsolecommand("E")
waitconsoleready();

vplusconsole.close()
f.close()
