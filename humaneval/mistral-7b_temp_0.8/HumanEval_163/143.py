
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Write your code here.
    if a == b:
        return []
    if a % 2 == 0 and b % 2 == 0:
        return [a, a + 2, a + 4, a + 6, b]
    if a % 2 == 0 and b % 2 != 0:
        return [a, a + 2, a + 4, a + 6]
    if a % 2 != 0 and b % 2 == 0:
        return [a + 2, a + 4, a + 6, b]
    if a % 2 != 0 and b % 2 != 0:
        return [a + 2, a + 4, a + 6]

