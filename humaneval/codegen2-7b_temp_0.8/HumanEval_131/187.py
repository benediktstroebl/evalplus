
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num = n
    total = 0
    while num > 0:
        if num % 2:
            total += num % 10
        num = num // 10
    return
