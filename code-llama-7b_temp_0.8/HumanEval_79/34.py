
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

    binary = bin(decimal)
    binary_list = list(binary)
    # Removing the first two characters of the list
    del binary_list[0]
    del binary_list[0]
    # Removing the last character of the list
    del binary_list[-1]
    # Adding 'db' at the beginning and at the end of the list
    binary_list.insert(0, 'b')
    binary_list.append('d')
    # Converting the list to a string
    binary_string = ''.join(binary_list)
    return binary_string
