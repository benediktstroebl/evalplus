
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
    # create the output string
    output = ""
    # determine if the decimal is negative or positive
    # make sure the decimal is positive
    if decimal < 0:
        negative = True
        decimal = abs(decimal)
    else:
        negative = False
    while decimal > 0:
        # take the remainder of the decimal by 2
        remainder = decimal % 2
        # reverse the string to make it easier to add to the output
        output = str(remainder) + output
        # add the remainder to the current decimal
        decimal = decimal // 2
        # add the remainder to the output
    if negative:
        output = "db" + output
    return output

