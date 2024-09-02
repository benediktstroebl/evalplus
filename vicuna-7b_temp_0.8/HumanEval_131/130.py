
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 1:
        return 0
    digits = []
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            digits.append(0)
        else:
            n = n // 2
            digits.append(1)
    result = 1
    for i in range(1, len(digits)):
        result *= digits[i]
    return result
