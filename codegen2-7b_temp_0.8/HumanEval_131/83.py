
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
    odds = n % 10
    n //= 10
    while n >= 10:
        odds *= (n % 10)
        n //= 10
    return odds if odd
