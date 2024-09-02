
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a == b:
        return []
    elif a > b:
        return []

    ints = [-1, -1]
    n = 0
    while n <= b:
        if n % 2 == 0:
            ints.append(n)
        n += 1
    return ints

