import pyautogui
import serial  # from pyserial package
import struct  # import to decode the byte strings returned form the serial read
with serial.Serial('COM3', 115200) as ser:
    # print(ser.readline())  # This should read to the first '\n' character
    # If you don't see anything on the output
    # it could be because the board did not send a line
    # try pressing the reset button to resend the string
    while True:
        # Read one character
        some_bytes = ser.read()

        # Returns a list (of length 1) of decoded python types
        decoded_bytes = struct.unpack('B', some_bytes)
        # NOTE: This code will throw an error if you send to fast because
        # some_bytes is too long and cant be decoded into a single 8-bit int

        num = int(decoded_bytes[0])
        print(num)
        if(num == 1):
            pyautogui.press('right')
            print("Right Pressed")
        elif(num == 2):
            pyautogui.press('left')
            print("Left Pressed")
        elif(num == 3):
            pyautogui.press('up')
            print("Up pressed")
        elif(num >= 40):
            pyautogui.press('space')
            print("Space pressed")
            print(num)
            # print("Did nothing")
