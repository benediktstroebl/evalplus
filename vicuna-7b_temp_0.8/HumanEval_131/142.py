
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n % 2 != 0:
        return n // 2
    digits = [n % 10]
    while n:
        if n % 2 == 0:
            digits.append(0)
        n = n // 10
        digits.append(10 - digits[-1])
    return sum(digits)
