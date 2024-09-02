
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    ints = []
    i = a
    while i <= b:
        if (i % 10) % 2 == 0:
            ints.append(i)
        i += 1
    return ints
