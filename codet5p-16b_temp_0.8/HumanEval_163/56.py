
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    l = []
    if a < 10:
        return l
    if a > b:
        return l
    if a % 2!= 0:
        return l
    else:
        while a <= b:
            if a % 2 == 0:
                l.append(a)
            a += 1
        return l













