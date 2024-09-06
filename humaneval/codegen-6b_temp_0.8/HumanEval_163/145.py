
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if not isinstance(a, (int, long)) or not isinstance(b, (int, long)):
        raise TypeError("Both arguments must be integers.")
    elif a > b:
        raise ValueError("a must be less than b.")
    elif a % 2 != 0 or b % 2 != 0:
        raise ValueError("Both arguments must be even.")
    else:
        return [i for i in xrange(a + 2, b + 2) if i % 2 == 0]

