
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = abs(n)
    digits = []
    while n:
        digits.append(n % 10)
        n = n // 10
    return sum(digits)
