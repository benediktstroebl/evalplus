
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if not a <= b:
        raise ValueError("First argument must be <= second argument.")
    if a % 2 == 0 and b % 2 == 0:
        return [a, b]
    return [a, b] + generate_integers(a + 1, b - 1)

