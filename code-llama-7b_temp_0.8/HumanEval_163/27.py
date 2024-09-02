
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    i = min(a, b)
    j = max(a, b)
    if i % 2 != 0:
        i = i + 1
    ints = []
    while i < j:
        if i % 2 == 0:
            ints.append(i)
        i = i + 1
    return ints

