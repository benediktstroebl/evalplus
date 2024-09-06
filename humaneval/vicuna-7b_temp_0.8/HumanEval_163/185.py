
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    digits = []
    while b > a:
        half = a + (b - a) // 2
        digits.extend(str(i) for i in range(half + 1))
        a = half
    digits.extend(str(i) for i in range(b - a))
    return digits
