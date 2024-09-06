
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
    # Your code here
    str = ""
    if decimal == 0:
        str = "db0"
    elif decimal == 1:
        str = "db1"

    while decimal > 1:
        str += str[-1]
        decimal //= 2

    return "db" + str

