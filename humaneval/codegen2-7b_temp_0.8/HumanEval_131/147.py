
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 0: return 0
    even = 0
    while n > 0:
        digit = n % 10
        if digit % 2!= 0:
            even *= digit
        n = n // 10
    return even
