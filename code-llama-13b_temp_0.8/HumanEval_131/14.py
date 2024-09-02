
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # return all(d % 2 for d in str(n)) * 0 or reduce(mul, [int(d) for d in str(n) if d % 2])
    return reduce(lambda x, y: x * y, [int(d) for d in str(n) if d % 2], 1)

