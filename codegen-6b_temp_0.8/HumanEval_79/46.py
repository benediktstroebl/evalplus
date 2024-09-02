
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
    bin_rep = []

    # Add 'db'
    bin_rep.append('db')

    while decimal > 0:

        # Get the remainder of the division
        div = decimal % 2

        # Append the remainder to the list
        bin_rep.append(str(div))

        # Decrement the decimal
        decimal = decimal // 2

    # Reverse the list
    bin_rep.reverse()

    # Add 'db' to the front and back of the string
    bin_rep.insert(0, 'db')
    bin_rep.append('db')

    # Return the string
    return ''.join(bin_rep)

