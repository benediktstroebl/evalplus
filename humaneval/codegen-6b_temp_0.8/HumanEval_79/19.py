
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
    # Check for empty string
    if decimal == "":
        return ""
    # Check for invalid values
    if not isinstance(decimal, int) or not (0 <= decimal <= 2147483647):
        return None

    binary = ""
    while decimal > 0:
        # Modulo to get the last 1 to get to 2**n
        binary = str(decimal % 2) + binary
        decimal = (decimal - 1) // 2
    # Add leading 0's
    binary = "0" * (32 - len(binary)) + binary
    return binary

