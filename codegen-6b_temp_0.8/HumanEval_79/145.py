
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
    decimal_binary = ""
    first_bit = "0"
    last_bit = "0"
    while decimal > 0:
        if decimal % 2 == 0:
            first_bit = "0" + first_bit
            last_bit = "1" + last_bit
        else:
            first_bit = "1" + first_bit
            last_bit = "0" + last_bit
        decimal = decimal // 2
    decimal_binary = first_bit + last_bit
    return "db" + decimal_binary + "db"
