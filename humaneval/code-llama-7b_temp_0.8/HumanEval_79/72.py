
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

    if decimal > 0:
        # Create an empty list to store the bits in
        binary_bits = []

        # While the decimal is greater than 0
        while decimal > 0:
            # Find the remainder
            remainder = decimal % 2

            # Add the remainder to the list
            binary_bits.append(remainder)

            # Divide by two and continue the loop
            decimal = decimal // 2

        # Join the list to make a string
        binary = ''.join(map(str, binary_bits))

        # Create a variable with the characters db to represent the beginning and end of the binary number
        binary_string = "db" + binary + "db"

        # return the string
        return binary_string

    # If the decimal is zero, return the string "db0db"
    else:
        return "db0db"

