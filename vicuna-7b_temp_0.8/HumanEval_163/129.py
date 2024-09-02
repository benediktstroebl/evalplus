
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if b <= a:
        return []
    if a % 2 != 0:
        # even digits are only in the second half
        return [int(x) for x in str(a)[a % 2 == 0]:]
    else:
        # all digits in the first half
        return [int(x) for x in str(a)]
