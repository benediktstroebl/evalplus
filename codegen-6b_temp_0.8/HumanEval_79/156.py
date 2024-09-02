
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
    
    binary = []
    # make a list with 0s until the decimal is 0, that's the length of the list
    while decimal > 0:
        binary.append(decimal % 2)
        decimal = decimal // 2
    # Swap the sign of the list
    binary.reverse()
    # add the sign to the front
    binary.insert(0,'-')
    # add the sign to the back
    binary.append('-')
    # convert the list to a string
    binary = ''.join(map(str, binary))
    return binary
