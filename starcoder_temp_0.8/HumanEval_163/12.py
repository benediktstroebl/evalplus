
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    def is_even(i):
        return i % 2 == 0

    def is_between(i):
        return a <= i <= b

    return [i for i in range(a, b+1) if is_even(i) and is_between(i)]

