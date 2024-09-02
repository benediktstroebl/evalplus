
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = abs(n)
    count = 0
    if n < 10:
        return n
    while n > 0:
        d = n % 10
        if d % 2 != 0:
            count += d
        n = n // 10
    return count
