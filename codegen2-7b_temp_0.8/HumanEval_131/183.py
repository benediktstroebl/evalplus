
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = []
    while n > 0:
        d = n % 10
        n = n // 10
        if not d % 2:
            digits.append(d)
    return int(sum(digits))
