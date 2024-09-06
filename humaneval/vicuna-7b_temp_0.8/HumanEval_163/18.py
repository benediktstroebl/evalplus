
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Create a set to store the even digits
    even_digits = set()

    # Loop through the range of integers from a to b
    for i in range(a, b+1):
        # If the current integer is even, add it to the set of even digits
        if i % 2 == 0:
            even_digits.add(i)

    # Return the set of even digits in ascending order
    return sorted(even_digits)
