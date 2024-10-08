
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

    # Your code goes here...

    # 0. put the number in string form
    binary_number = str(decimal)

    # 1. remove all the digits except the last digit
    binary_number = binary_number[0:1]

    # 2. put 'db' before and after the binary number
    binary_number = 'db' + binary_number + 'db'

    return binary_number
