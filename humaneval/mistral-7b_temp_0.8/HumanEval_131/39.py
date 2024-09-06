
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    d = []
    while n > 0:
        r = n % 10
        if r % 2 == 1:
            d.append(r)
        n = n // 10
    if len(d) > 0:
        return reduce(lambda x,y: x * y, d)
    else:
        return 0
