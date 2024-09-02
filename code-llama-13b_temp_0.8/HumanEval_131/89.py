
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 10:
        return n
    digit = n % 10
    if digit % 2 != 0:
        return digit * digits(n // 10)
    return digits(n // 10)
