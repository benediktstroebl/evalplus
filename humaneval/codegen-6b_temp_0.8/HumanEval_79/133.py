
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
    # TODO: Your code here.
    if not isinstance(decimal, int):
        raise TypeError("num must be an integer")
    if decimal < 0:
        raise ValueError("num must be positive")
    decimal_bin = []
    while decimal > 0:
        decimal, mod = divmod(decimal, 2)
        decimal_bin.insert(0, str(mod))
    return ''.join(decimal_bin)

