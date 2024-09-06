
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    digit_list = [int(i) for i in str(n)]
    product = 1
    for digit in digit_list:
        if digit % 2!= 0:
            product *= digit
    return product
