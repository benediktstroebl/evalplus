
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    d = [int(i) for i in str(a)]
    while len(d) > 0:
        d.pop(0)
    d.extend([int(i) for i in str(b)])
    return d
