
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
    binary = 'db'
    if decimal <= 1:
        binary += '0'
    elif decimal <= 2:
        binary += '1'
    elif decimal <= 4:
        binary += '10'
    elif decimal <= 8:
        binary += '11'
    elif decimal <= 16:
        binary += '100'
    elif decimal <= 32:
        binary += '101'
    elif decimal <= 64:
        binary += '110'
    elif decimal <= 128:
        binary += '111'
    elif decimal <= 256:
        binary += '1000'
    elif decimal <= 512:
        binary += '1001'
    elif decimal <= 1024:
        binary += '1010'
    elif decimal <= 2048:
        binary += '1011'
    elif decimal <= 4096:
        binary += '1100'
    elif decimal <= 8192:
