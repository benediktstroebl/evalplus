
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
    
    # Initialise output from front and back to be a string of length 10
    binary_front = "db"
    binary_back = "db"
    
    # Initialise the output string
    binary = ""

    # Loop until we have at least 1 bit
    while len(binary) < 10:
        
        # Shrink the decimal number, obtain the remainder, and add it to the binary representation
        decimal, remainder = divmod(decimal,2)
        binary += str(remainder)

    # Reverse it
    binary = binary[::-1]

    # We return the front and back parts plus the string of bits
    return binary_front + binary + binary_back
