
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # remove the even digits
    while n % 2 == 0:
        n //= 2
    # remove all other digits
    while n % 2 == 1:
        n //= 2
        n = (n // 10) * (n % 10)
    return n
