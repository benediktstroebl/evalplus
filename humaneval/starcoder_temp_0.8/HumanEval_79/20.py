
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
    # Convert decimal to binary
    bin_list = []
    while decimal!= 0:
        bin_list.append(decimal % 2)
        decimal = decimal // 2
    bin_list.reverse()
    bin_string = ''.join([str(i) for i in bin_list])
    # Add extra 'db's
    return 'db' + bin_string + 'db'
