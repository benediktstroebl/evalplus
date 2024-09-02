
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # check that a and b are valid
    if not (a > 0 and b > 0 and a <= b):
        raise ValueError("invalid arguments")

    # check that a and b are different
    if a == b:
        return []

    # check if a and b are the same
    if a == b - 1:
        return [a]

    # a and b are not the same, check that a < b
    if a > b:
        return generate_integers(b, a)

    # a and b are different and in ascending order, find the result recursively
    return [a] + generate_integers(a + 2, b)

