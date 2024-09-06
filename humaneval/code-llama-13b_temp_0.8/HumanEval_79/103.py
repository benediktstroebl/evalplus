
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
    # Step 1: Convert the decimal value to binary value
    # Step 2: Make a binary string from the binary value
    # Step 3: Add the "db" to the binary string
    binary = bin(decimal)
    binary_string = str(binary)[2:]
    result = "db" + binary_string + "db"
    return result

