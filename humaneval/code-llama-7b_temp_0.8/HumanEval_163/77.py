
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if (a % 2 == 1):
        a += 1
    if (b % 2 == 1):
        b += 1
    ret = []
    if (a <= b):
        for x in range(a, b + 1, 2):
            ret.append(x)
    else:
        for x in range(b, a + 1, 2):
            ret.append(x)
    return ret
