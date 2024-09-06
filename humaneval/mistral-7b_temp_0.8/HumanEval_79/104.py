
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

    db = 'db'

    dec_list = []
    for digit in str(decimal):
        dec_list.append(digit)

    binary_list = []

    for digit in reversed(dec_list):
        binary_list.append(int(digit))

    binary = ''
    for digit in binary_list:
        binary += str(digit)

    if binary_list[-1] == 0:
        binary = '0' + binary

    return db + binary + 'db'

