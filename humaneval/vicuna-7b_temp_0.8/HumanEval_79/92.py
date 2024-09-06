
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
    # initialize variables to store the binary number
    left = '0'
    right = '0'
    result = '0'

    # loop through decimal number and convert it into binary
    while decimal > 0:
        # divide the decimal number by 2
        right = str(int(right) / 2)
        decimal = int(decimal) % 2

        # add the left and right binary numbers
        result = str(left) + str(right)

        # add the next digit of the binary number
        left = '0' if left == '1' else '1'

    # add the extra characters 'db' at the beginning and end of the binary number
    return 'db' + result + 'db'
