
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

    binary_list = []
    binary_string = ''

    decimal_int = decimal
    binary_string = ''

    # While decimal_int is greater than 0
    while decimal_int > 0:
        quotient = decimal_int // 2
        remainder = decimal_int % 2
        decimal_int = quotient

        binary_list.append(remainder)

    binary_list.reverse()

    # convert binary list to a string and append to beginning of string
    for i in binary_list:
        binary_string += str(i)

    return 'db' + binary_string + 'db'

