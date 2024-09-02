
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = int(n)
    if n % 2 == 0:
        return 0
    result = 1
    for i in range(1, n//2+1):
        result *= n % 10
    return result
