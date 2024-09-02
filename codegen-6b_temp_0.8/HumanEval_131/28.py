
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # use divmod and mod to find the highest and mod of the product
    odd_digit_product = 1
    for highest, mod in divmod(n, 10):
        if mod % 2:
            odd_digit_product *= highest
    return odd_digit_product

