
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = list(str(n))
    result = 1
    for digit in digits:
        if int(digit) % 2!= 0:
            result *= int(digit)
    return result
