
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    result = 1
    for i in range(len(str(n)) // 2):
        if n % 10 ** i == 1:
            result *= 10 ** i
    return result
