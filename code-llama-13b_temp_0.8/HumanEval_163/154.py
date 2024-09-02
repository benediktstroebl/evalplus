
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def is_even(n):
        return n % 2 == 0

    def even_digits(n):
        return list(filter(is_even, [int(i) for i in str(n)]))

    return sorted(list(set(even_digits(n)) for n in range(a, b + 1)))

