
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
    # first convert decimal to binary and get the length of the binary string
    binary = str(decimal).zfill(base=2)
    binary_len = len(binary)

    # initialize the result string
    result = ''

    # loop over each digit in the binary string
    for i in range(binary_len):
        # add '1' to the result if the current digit is a '1'
        if binary[i] == '1':
            result += '1'
        else:
            result += '0'

    # append 'db' to the beginning and the result to the string
    result = 'db' + result

    return result
