
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    total_product = 1
    for i in range(0, len(str(n))):
        digit = n % 10
        if digit % 2 == 1:
            total_product *= digit
    return total_product

