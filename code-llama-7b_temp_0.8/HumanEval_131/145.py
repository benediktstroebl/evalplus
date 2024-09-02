
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = int(n)
    res = 1
    while n > 0:
        temp = n % 10
        if temp % 2 != 0:
            res *= temp
        n = n // 10
    return res

