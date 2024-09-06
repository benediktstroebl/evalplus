
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
    # Convert the given decimal number to binary string
    binary_string = bin(decimal)[2:]

    # Add extra characters 'db' at the beginning and end of the binary string
    binary_string = 'db' + binary_string + 'db'

    # Convert each character in the binary string to its corresponding ASCII code
    ascii_codes = [ord(char) for char in binary_string]

    # Return the string with each character representing the corresponding ASCII code
    return ''.join([chr(code) for code in ascii_codes])
