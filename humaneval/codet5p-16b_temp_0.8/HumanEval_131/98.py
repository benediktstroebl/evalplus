
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    digits = 1
    if n < 1:
        raise ValueError("Number should be positive")
    for num in str(n):
        if int(num) % 2!= 0:
            digits *= int(num)
    return digits
