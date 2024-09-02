
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a <= b:
        lower, upper = a, b
    else:
        lower, upper = b, a

    if lower % 2 != 0:
        lower += 1

    if upper % 2 != 0:
        upper -= 1

    return [i for i in range(lower, upper + 1, 2)]
