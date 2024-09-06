
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """

    # variable to store the binary string
    binary = ''

    # loop through the decimal digits
    while decimal > 0:
        # convert the decimal digit to binary
        binary_digit = decimal % 2

        # add the binary digit to the binary string
        binary += str(binary_digit)

        # divide the decimal by 2
        decimal = int(decimal / 2)

    # add the 'db' characters to the beginning and end of the binary string
    binary = 'db' + binary + 'db'

    return binary