
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
    # create a list to store the decimal digits
    decimal_list = []
    while decimal!= 0:
        # store the last digit of the decimal number
        decimal_list.append(decimal % 2)
        # truncate the decimal number
        decimal = decimal // 2
    # add a couple of extra characters to the start and end of the list
    decimal_list.append("db")
    decimal_list.insert(0, "db")
    return "".join([str(digit) for digit in decimal_list])
