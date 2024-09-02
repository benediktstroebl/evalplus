
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
    # TODO: Write your code here
    # Use a loop to convert decimal number to binary
    decimal_string = str(decimal)
    decimal_binary = []
    while decimal_string:
        decimal_binary.append(int(decimal_string[-1]))
        decimal_string = decimal_string[:-1]
    binary_string = ""
    for i in decimal_binary:
        binary_string += str(i)
    return 'db' + binary_string + 'db'

