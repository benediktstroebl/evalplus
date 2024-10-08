
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    result = 1
    while n:
        i = n % 10
        n = n // 10
        if i % 2 == 1:
            result = result * i
    return result

