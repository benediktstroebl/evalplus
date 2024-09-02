
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a < 2 or b < 2:
        return []

    # The idea is firstly, we generate all the integers from a to b, using the
    # generators module. Then only keep the even digits.
    integers = filter(lambda i: i % 2 == 0, range(a, b + 1))
    return integers

