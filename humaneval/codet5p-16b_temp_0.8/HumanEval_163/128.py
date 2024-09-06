
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    res = []
    for x in range(a, b+1):
        if x % 2 == 0 and str(x).zfill(2)[0]!= '0':
            res.append(int(str(x).zfill(2)))
    return sorted(res)

