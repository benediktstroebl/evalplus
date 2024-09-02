
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if b % 10 == 0:
        return []
    if a % 10 < b % 10:
        return [x for x in range(a, b+(10-a%10), 10)]
    else:
        return [x for x in range(b-1, a-1, -10)]

