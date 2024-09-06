
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

    binary = "db"

    if decimal < 0:
        return "db"

    elif decimal == 0:
        return "db"

    elif decimal == 1:
        return "db1"

    elif decimal == 2:
        return "db10"

    elif decimal == 3:
        return "db11"

    elif decimal == 4:
        return "db100"

    elif decimal == 5:
        return "db101"

    elif decimal == 6:
        return "db110"

    elif decimal == 7:
        return "db111"

    elif decimal == 8:
        return "db1000"

    elif decimal == 9:
        return "db1001"

    elif decimal == 10:
        return "db1010"

    elif decimal == 11:
        return "db1011"

    elif decimal == 12:
        return "db1100
