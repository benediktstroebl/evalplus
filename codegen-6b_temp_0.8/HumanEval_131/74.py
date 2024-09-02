
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def digit(d, n):
        return (d - 2) * (n // (d - 2))

    return reduce(lambda x, y: x * y, map(digit, range(1, 10, 2), itertools.count(n, 2)))
