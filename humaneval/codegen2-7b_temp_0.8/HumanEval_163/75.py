
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    a, b = sorted([a, b])
    if a % 2 == 1 and b % 2 == 0:
        return generate_integers(a, b-1) + [b]
    if a % 2 == 0 and b % 2 == 1:
        return generate_integers(a+1, b)
    return generate_integers(a+1, b-1) + [b]

