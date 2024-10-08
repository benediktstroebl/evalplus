
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False
    return list(filter(is_even, range(min(a,b), max(a,b)+1)))
