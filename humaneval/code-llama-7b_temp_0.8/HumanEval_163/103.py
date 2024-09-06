
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # destructuring assignment, for python 3.5
    # a, b = 8, 2
    #
    # a, b = b, a
    #
    # a, b = 2, 8

    a, b = (a, b) if a < b else (b, a)

    if a % 2 == 1:
        a += 1

    return list(range(a, b+1, 2))

