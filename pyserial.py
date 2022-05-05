import serial  # from pyserial package
import struct  # import to decode the byte strings returned form the serial read
with serial.Serial('COM15', 115200) as ser:
    print(ser.readline())  # This should read to the first '\n' character
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

        print(f'{some_bytes} decodes to the number: {decoded_bytes[0]}')
