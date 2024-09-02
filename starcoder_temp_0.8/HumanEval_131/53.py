
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if not isinstance(n, int):
        raise ValueError("n must be positive integer")

    if n <= 0:
        raise ValueError("n must be positive integer")

    mult = 1
    for d in str(n):
        if int(d) % 2:
            mult *= int(d)

    return mult

