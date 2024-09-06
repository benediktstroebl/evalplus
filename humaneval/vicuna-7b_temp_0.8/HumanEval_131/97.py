
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n % 10 != 0:
        return n
    digits = []
    while n > 0:
        if n % 10 != 0:
            digits.append(n % 10)
            n = n // 10
        else:
            digits.append(n)
            n = 0
    return sum(digits)
