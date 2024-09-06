
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = 1
    while n:
        if n % 10 % 2 == 0:
            break
        digits *= 10
        n //= 10
    return digits
