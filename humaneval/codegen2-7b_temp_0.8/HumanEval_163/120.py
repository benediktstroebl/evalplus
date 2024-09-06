
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a >= b:
        return []
    if b % 2 == 0:
        return [b]
    return generate_integers(a, b + 1) + generate_integers(a + 1, b)

