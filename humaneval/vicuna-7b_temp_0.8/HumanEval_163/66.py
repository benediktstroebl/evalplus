
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # If a is less than b, the function should return an empty list
    if a <= b:
        return []
    # Otherwise, iterate over the digits of a
    for i in range(10):
        d = a // 10**i
        if d % 2 == 0:
            return [str(i)] + generate_integers(a, d)
    # If we reach this point, b has only odd digits
    return [str(i)] + generate_integers(a, b)
