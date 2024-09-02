
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
    decimal = str(decimal)

    if decimal.startswith('-'):
        sign = '-'
        decimal = decimal[1:]
    else:
        sign = ''

    result = ''

    for i, char in enumerate(decimal[::-1]):
        result += digits[int(char)]

        if i % 4 == 3 and i!= len(decimal) - 1:
            result += 'db'

    result += 'db'

    if sign == '-':
        result = '-' + result[1:]

    return result
