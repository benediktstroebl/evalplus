
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num = n
    p = 1
    while (num!= 0):
        r = num % 10
        if r % 2 == 0:
            num = num // 10
            continue
        p = p * r
        num = num // 10
    return p

