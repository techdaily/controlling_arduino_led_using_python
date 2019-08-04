import serial  # add Serial library for Serial communication

Arduino_Serial = serial.Serial('com3', 9600)  # Create Serial port object called arduinoSerialData

print("Enter 1 to ON LED and 0 to OFF LED")

while 1:  # infinite loop
    input_data = input()  # waits until user enters data
    print("you entered", input_data)  # prints the data for confirmation

    if (input_data == '1'):  # if the entered data is 1
        Arduino_Serial.write(str.encode('1'))  # send 1 to arduino
        print("LED ON")

    if (input_data == '0'):  # if the entered data is 0
        Arduino_Serial.write(str.encode('0'))  # send 0 to arduino
        print("LED OFF")