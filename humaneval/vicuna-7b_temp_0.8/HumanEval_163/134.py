
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # remove numbers of 0
    a, b = max(a, b), min(a, b)

    if b - a == 1:
        return [a, b]
    while b > a:
        a, b = next_high(a, b)

    def next_high(x):
        if x == 1:
            return 2
        return x + 1

    def is_even(x):
        return x % 2 == 0

    digits = [int(str(x)) for x in range(a, b + 1)]
    digits = [d for d in digits if is_even(d)]
    digits.sort()
    return digits
