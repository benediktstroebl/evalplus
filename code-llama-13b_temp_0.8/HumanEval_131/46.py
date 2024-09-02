
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = [int(x) for x in str(n) if int(x) % 2 == 1]
    if len(digits) > 0:
        product = 1
        for digit in digits:
            product *= digit
        return product
    return 0

