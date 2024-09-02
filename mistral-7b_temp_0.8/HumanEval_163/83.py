
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
        return x % 2 == 0

    def is_between(x, low, high):
        return x >= low and x <= high

    if b <= a:
        return []

    return list(filter(is_even, filter(is_between, range(a, b + 1))))

