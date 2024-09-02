
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # If the range is 0 <= a <= b, there are no even digits to generate
    if a <= b:
        return []
    # Initialize the list of even digits to []
    even_digits = []
    # Iterate over the range a <= x <= b
    for x in range(a, b+1):
        # If x is even, append it to the list of even digits
        if x % 2 == 0:
            even_digits.append(x)
    # Return the list of even digits in ascending order
    return even_digits
