
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    def get_digits(n):
        while n != 0:
            yield n % 10
            n //= 10

    product = 1
    digits = get_digits(n)
    for d in digits:
        if d % 2 == 1:
            product *= d
    return product


