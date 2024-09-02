
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
    assert isinstance(decimal, int), "Input is not an integer"
    assert 0 <= decimal <= (2 ** 8 - 1), "Input must be in range [0, 255]"
    binary_string = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary_string = str(remainder) + binary_string
    binary_string = "db" + binary_string
    return binary_string

