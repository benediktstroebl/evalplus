
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
    global digit
    if decimal < 0:
        raise ValueError("A non-negative integer is required.")

    binary = [0] * (digit + 1)

    for i in range(digit + 1):
        binary[i] = decimal % 2
        decimal //= 2

    return "".join(str(x) for x in binary[::-1])

