
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    i = 0
    while n > 0:
        if n % 10 % 2 == 1:
            product *= n % 10
        n /= 10
        i += 1
    return product if i > 0 else 0
