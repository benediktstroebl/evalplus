
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = int(n)
    if n < 1:
        return 0
    if n % 2 == 0:
        return 0
    result = n
    while n > 0:
        if n % 2 != 0:
            result = (result * 10) + (n // 2)
        n = n // 2
    return result
