
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
    # This function is hardcoded, which means it doesn't handle the case where the input is not
    # an integer. It only works with integers.
    # You can use the `int` function to convert the input to an integer.
    # If you want to handle the case where the input is not an integer, you can use the `isinstance`
    # function to check if the input is an integer or not.

    # The rest of the function uses the `format` method to convert the decimal number to binary.
    # The format method takes a string as an argument, which is a placeholder for the different
    # types of data that you want to display. In this case, we use the format method to
    # display each decimal digit as a binary digit, and we also use the format method to add
    # the extra characters 'db' at the beginning and at the end of the string.

    # Here's the code for the rest of the function:
    digits = '01'
    binary = ''
    while decimal > 0:
        binary = digits[int(decimal % 2) + 1] + binary
        decimal //= 2
    return 'db' + binary + 'db'
