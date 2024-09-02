
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num = n
    if n < 0:
        n = abs(n)
    product = 1
    while n > 0:
        if n % 2 == 0:
            n = n // 10
            continue
        digit = n % 10
        product *= digit
        n = n // 10
    return product

