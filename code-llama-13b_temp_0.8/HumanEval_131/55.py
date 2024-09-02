
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
    else:
        s = str(n)
        res = 1
        for c in s:
            c = int(c)
            if c % 2 == 0:
                res *= c
        return res

