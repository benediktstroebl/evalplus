
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Check if b is less than a
    if b < a:
        return []

    # Create a list to store the even digits
    even_integers = []

    # Iterate from a to b, checking if the current digit is even
    for i in range(a, b+1):
        # Extract the rightmost digit of the current integer
        digit = i % 10

        # If the digit is even, add it to the list of even integers
        if digit % 2 == 0:
            even_integers.append(digit)

    # Sort the list of even integers in ascending order
    even_integers.sort()

    # Return the list of even integers
    return even_integers

