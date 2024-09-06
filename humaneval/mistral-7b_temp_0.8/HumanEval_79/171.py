
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
    number = []
    if decimal < 0:
        decimal = decimal * -1
        number.append('-')
    if decimal == 0:
        number.append('0')
    else:
        while decimal != 0:
            number.append(str(decimal % 2))
            decimal = decimal // 2
    number.reverse()
    number.append('db')
    number.append('db')
    number = ''.join(number)
    return number

