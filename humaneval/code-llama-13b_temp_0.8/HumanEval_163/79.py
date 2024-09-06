
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    is_even = lambda x: x % 2 == 0
    between = lambda x, y: a <= x and x <= b

    even_numbers = filter(is_even, range(a, b+1))
    even_numbers_between = filter(between, even_numbers)

    return sorted(even_numbers_between)
