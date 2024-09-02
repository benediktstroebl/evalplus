
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    total = 1
    for i in range(len(str(n))):
        m = n // 10 ** (len(str(n))-i-1)
        total *= m % 2
    return total

