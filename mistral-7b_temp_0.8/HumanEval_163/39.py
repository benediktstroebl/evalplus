
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        return generate_integers(b, a)
    if a % 2 != 0 and b % 2 != 0:
        return []
    if a % 2 == 0 and b % 2 == 0:
        if a == b:
            return [a]
        if b - a == 1:
            return [a, b]
        return [a, b] + generate_integers(a + 2, b - 2)
    elif a % 2 == 0:
        return [a] + generate_integers(a + 2, b - 2)
    elif b % 2 == 0:
        return [b] + generate_integers(a + 2, b - 2)

