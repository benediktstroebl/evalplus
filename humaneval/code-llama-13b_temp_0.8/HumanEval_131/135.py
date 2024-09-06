
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    s = str(n)
    prod = 1
    for ch in s:
        i = int(ch)
        if i % 2 != 0:
            prod *= i
    return prod
