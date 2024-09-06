
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n, d = abs(n), 1
    while n:
        d *= n % 10
        n //= 10
    return d if n == 1 else 0

