
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

    def between(x, y):
        return a <= x and x <= b

    return [n for n in range(a, b+1) if is_even(n) and between(n, b)]

    # or 
    # return sorted(set(filter(lambda x: x%2 == 0 and a <= x and x <= b, range(a,b+1))))
