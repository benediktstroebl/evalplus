
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    assert a > 0
    assert b > 0

    if a > b:
        start, end = b, a
    else:
        start, end = a, b

    # Filter and map
    return list(filter(lambda n: not n % 2, range(start, end + 1)))

