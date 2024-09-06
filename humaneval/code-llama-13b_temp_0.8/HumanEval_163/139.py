
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    from math import ceil

    def last_digit(x):
        return x % 10

    def next_digit(x):
        return x // 10

    def is_even(x):
        return x % 2 == 0

    def collect_numbers(result, x, y):
        if x == y:
            return result
        if is_even(last_digit(x)):
            result.append(last_digit(x))
        return collect_numbers(result, next_digit(x), y)

    if a > b:
        return collect_numbers([], ceil(b / 10), ceil(a / 10))
    return collect_numbers([], ceil(a / 10), ceil(b / 10))

