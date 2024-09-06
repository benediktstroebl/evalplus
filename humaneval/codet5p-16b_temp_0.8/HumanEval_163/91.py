
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    a = str(a)
    b = str(b)
    evens = []
    for n in range(int(a), int(b) + 1):
        if int(n) % 2 == 0:
            evens.append(n)
    return evens
