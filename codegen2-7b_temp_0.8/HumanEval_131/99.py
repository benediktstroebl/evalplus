
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    dig = 1
    for i in range(1, n + 1):
        dig *= i % 10
        if i % 2:
            dig *= 9
    return
