import serial
ser = serial.Serial(22, 9600)
ser.write('hey' + '\\n')
ret = ser.read(10)
print ret
ser.close()