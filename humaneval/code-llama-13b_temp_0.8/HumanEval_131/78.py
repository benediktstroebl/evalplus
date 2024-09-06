
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 0:
        return 0

    if not n % 2:
        return 0

    if n < 10:
        return n

    num_odd = 1
    while n:
        digit = n % 10
        n = n // 10
        if digit % 2 != 0:
            num_odd *= digit
    return num_odd

