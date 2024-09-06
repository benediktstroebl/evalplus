
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    assert a > 0 and b > 0, "a and b must be positive"

    # to avoid doing the same code twice, swap a and b if a is bigger than b
    if a > b:
        a, b = b, a

    return [x for x in range(a, b + 1) if x % 2 == 0]

