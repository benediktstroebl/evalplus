
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
    assert type(decimal) == int, "The function takes only a single integer as input"
    assert decimal >= 0, "The input cannot be negative"
    bin_str = ""
    while decimal >= 1:
        bin_str += str(decimal % 2)
        decimal = decimal // 2
    return "db" + bin_str[::-1] + "db"
