
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    a -= 1
    b -= 1
    diff = b - a + 1
    return [i + a for i in range(diff) if i % 2 == 0 and a <= i <= b]

