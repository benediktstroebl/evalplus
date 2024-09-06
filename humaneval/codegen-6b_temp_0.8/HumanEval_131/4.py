
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    odd = 0
    while n > 0:
        if n % 10 % 2 == 1:
            product = product * n % 10
            odd += 1
        n = n // 10
    return product if odd > 0 else 0
