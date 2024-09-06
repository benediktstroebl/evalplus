
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 0:
        return 0
    elif n == 0:
        return 0
    else:
        res = 1
        while n > 0:
            res *= n % 10
            n //= 10
        return res
