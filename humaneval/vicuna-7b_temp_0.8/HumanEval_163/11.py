
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    while b > a:
        n = a
        a = b
        b = n // 2
        result.append(a)
    while a > 0:
        result.append(a)
        a = a - 1
    return result