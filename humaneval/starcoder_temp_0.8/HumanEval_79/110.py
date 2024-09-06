
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
    num_bits = math.ceil(math.log(decimal, 2)) + 1
    binary_array = [0] * num_bits
    i = 0
    while decimal:
        binary_array[i] = decimal % 2
        decimal //= 2
        i += 1

    return 'db' + ''.join(str(bit) for bit in reversed(binary_array)) + 'db'

