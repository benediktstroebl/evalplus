
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
    if type(decimal) != int:
        raise TypeError("decimal must be an integer")
    if decimal < 0 or decimal > 255:
        raise ValueError("decimal must be between 0 and 255")

    binary = []
    bin_str = ""
    while decimal:
        decimal, i = divmod(decimal, 2)
        binary.append(str(i))
    binary.reverse()

    for digit in binary:
        bin_str += digit

    return "db" + bin_str + "db"

