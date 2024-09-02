
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digit_product = 0
    digits_list = list(str(n))
    for digit in digits_list:
        if int(digit) % 2 == 0:
            continue
        digit_product *= int(digit)
    return digit_product

