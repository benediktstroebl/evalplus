
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
    if isinstance(decimal, int):
        decimal = str(decimal)
    elif not isinstance(decimal, str):
        raise ValueError('Invalid input, must be a number')

    if 'db' in decimal:
        raise ValueError('Input is not decimal, it contains extra characters')

    if decimal == '0':
        return 'db0db'

    result = []
    while decimal!= '0':
        result.append('db' + ('1' if decimal[-1] == '1' else '0') + 'db')
        decimal = str(int(decimal) // 2)
    return ''.join(result[::-1])

