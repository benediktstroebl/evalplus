
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Store the even digits in a list
    digits = []

    # Loop over the range of integers from a to b (inclusive of a and exclusive of b)
    for i in range(a, b+1):
        # If the current digit is even, append it to the list
        if i % 2 == 0:
            digits.append(i)

    return digits
