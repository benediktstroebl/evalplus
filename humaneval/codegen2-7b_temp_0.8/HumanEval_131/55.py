
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    i = 2
    while n > 0:
        if n % i == 0:
            n = n / i
        else:
            i = i + 2
    if n == 0:
        return n
    else:
        return
