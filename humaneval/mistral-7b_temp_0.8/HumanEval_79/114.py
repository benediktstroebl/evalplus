
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

    # Your code here
    # Convert the decimal number to binary using the appropriate function.
    # Then extract the 8 binary characters from the binary string.
    # Use the string "db" as a prefix and suffix.

    binStr = "{0:b}".format(decimal)

    binNum = ""
    for i in range(len(binStr)-1):
        if binStr[i] == "1":
            binNum += "1"
        else:
            binNum += "0"

    return "db" + binNum + "db"
