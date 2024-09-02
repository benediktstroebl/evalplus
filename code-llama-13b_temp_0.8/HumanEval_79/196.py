
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
    # The binary value of the number is stored in the binary_value string
    binary_value = ""
    # The current value of the number to be converted to binary,
    # initially set to the number given as argument
    current_value = decimal
    while current_value > 0:
        binary_value = str(current_value % 2) + binary_value
        current_value = current_value // 2
    # Add the "db" at the beginning and at the end of the string
    return "db" + binary_value + "db"

