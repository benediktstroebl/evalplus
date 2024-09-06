
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    n = abs(n)
    digit_product = 1
    for i in str(n):
        if int(i) % 2!= 0:
            digit_product *= int(i)
    return digit_product
