
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    def is_odd(n):
        return n % 2 != 0

    def get_digit(n, i):
        return n % (10 ** (i + 1)) / (10 ** i)

    if n < 0:
        raise ValueError("Only positive integers allowed")

    if n == 0:
        return 0

    product = 1
    for i in range(0, len(str(n))):
        if is_odd(get_digit(n, i)):
            product *= get_digit(n, i)

    return product
