
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Define the range of integers to generate
    a = max(a, b)
    b = min(b, a)

    # Define the empty list to store the even digits
    digits = []

    # Generate the even digits in ascending order
    for i in range(a, b + 1):
        digits.append(i)

    return digits
