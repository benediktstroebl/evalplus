
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    res = 1
    n = str(n)
    for i in range(len(n)):
        if int(n[i]) % 2:
            res *= int(n[i])
    return res

