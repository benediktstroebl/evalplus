
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if not n % 2:
        return 0
    result = 1
    for i in range(1, len(str(n))):
        if n % 10 == 0:
            break
        result *= 10
        result += n % 10
    return result
