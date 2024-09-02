
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    #Your code here
    product = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    while n > 0:
        rem = n % 10
        if rem % 2 == 1:
            product *= rem
        n = n // 10
    return product

