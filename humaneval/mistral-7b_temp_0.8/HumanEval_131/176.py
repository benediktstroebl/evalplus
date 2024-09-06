
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    arr = [int(i) for i in str(n)]
    product = 1
    for i in arr:
        if i % 2 == 1:
            product *= i
    return product if product != 0 else 0

