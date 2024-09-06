
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    i = 1
    odd_product = 1
    while i <= n:
        if i % 2!= 0:
            odd_product *= i
        i += 1
    return odd_product
