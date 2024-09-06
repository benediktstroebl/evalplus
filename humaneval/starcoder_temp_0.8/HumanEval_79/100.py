
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

    binary_number = ''

    for digit in str(decimal):
        binary_digit = str(bin(int(digit)))[2:]
        if len(binary_digit) < 4:
            binary_digit = binary_digit.zfill(4)
        binary_number += binary_digit

    binary_number = 'db' + binary_number + 'db'
    return binary_number

