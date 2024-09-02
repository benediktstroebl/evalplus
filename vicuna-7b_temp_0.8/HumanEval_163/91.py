
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Find the sum of a and b
    c = a + b
    # Find the digit at the position of the sum in base 10
    digit = 10 * c // 10
    # Extract the even digit from the digit
    return digit % 2 == 0
