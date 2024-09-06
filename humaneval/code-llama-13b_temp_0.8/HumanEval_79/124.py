
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

    def bits(decimal):
        """ Convert a decimal number to binary using bitwise operators

        The bitwise operator ~ inverts the bits in a value. If we take the two's complement of the binary number,
        i.e. we invert the bits and add 1, we can obtain the binary number.

        The bitwise operator >> shifts the bits in a number to the right. The bits that are shifted out are lost.
        If the number was negative, the bits that are shifted in on the left side are 1's, if the number was positive,
        the bits that are shifted in on the left side are 0's.

        We can use these two operators to convert a decimal number to binary. The algorithm works as follows:
        1. Start with the number we want to convert to binary
        2. Invert the bits in the number
        3. Add 1 to the number
        4. Repeat step 2 and 3, until the number is no longer negative
        5. Remove the 1 in the beginning
        """
        binary = ~decimal
        while binary < 0:
            binary += 1
        binary = binary >> 1
        return binary

    return "db{0}db".format(bin(decimal)[2:])

