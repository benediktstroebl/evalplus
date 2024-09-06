
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

    # Your code goes here.

    # There is more than one way to solve this exercise.
    # A sample solution is provided below.
    # You can choose to use a built-in function or create your own.
    # Convert the decimal number to a binary number using the built-in bin function.
    binary = bin(decimal)

    # Remove the first two characters '0b'
    binary = binary[2:]

    # Loop over the characters in binary.
    # For each character, if the character is a 1, add it to the list called binary_numbers.
    # If the character is a 0, add a space to the list called binary_numbers.
    # The final result should be a list of 1's and 0's.
    binary_numbers = []
    for character in binary:
        if character == '1':
            binary_numbers.append(character)
        else:
            binary_numbers.append(" ")

    # Join the list to make a string.
    # It should be a string of 1's and 0's.
    binary = "".join(binary_numbers)

    # Add the extra characters to the beginning and end of the string.
    binary = "db" + binary + "db"

    # Return the binary string.
    return binary

