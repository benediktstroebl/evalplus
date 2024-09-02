
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    digits = list(str(n))
    for number in digits:
        if int(number) % 2 == 1:
            product *= int(number)
    return product
