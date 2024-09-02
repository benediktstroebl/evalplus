
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
        return [int(x) for x in str(n) if is_even(int(x))]

    def next_integer(n):
        return n + 1

    def has_reached_limit(n, limit):
        return n > limit

    def collect(acc, n):
        return acc + [n]

    return list(fold_right(collect,
                           filter(lambda x: len(x) > 0,
                                  map(even_digits,
                                      take_while(lambda n: not has_reached_limit(n, b),
                                                iterate(next_integer, a)))),
                           []))

