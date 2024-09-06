
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    s = str(n)
    i = 1
    j = len(s) - 1
    prod = 1
    while i <= j:
        t = int(s[i])
        if t % 2 != 0:
            prod *= t
        i += 1
        j -= 1
    return prod

