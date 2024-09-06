
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def generate_int(n, m):
        return [int(str(x)[:2]) for x in range(n, m) if is_even(x)]

    return generate_int(a, b)

