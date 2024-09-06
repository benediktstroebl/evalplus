
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if n <= 10:
        return 0

    m = 1
    for d in str(n):
        if int(d) % 2:
            m *= int(d)
    return m

