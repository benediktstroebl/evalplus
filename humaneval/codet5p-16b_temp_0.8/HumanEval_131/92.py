
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    total = 0
    if n % 2!= 0:
        return n
    while n > 0:
        total = total * 10
        n = n // 10
    return total
