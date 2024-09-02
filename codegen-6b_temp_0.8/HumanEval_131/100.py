
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = abs(n)
    mark = n % 10
    if mark == 0:
        return 0
    if mark == 1:
        return 1
    if mark == 9:
        return 9
    if mark % 2 == 0:
        return 0
    return mark * digits(n // 10)
