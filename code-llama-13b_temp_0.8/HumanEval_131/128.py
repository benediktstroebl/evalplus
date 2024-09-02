
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if not isinstance(n, int) or n < 1:
        raise TypeError("The input must be a positive integer!")
    result = 1
    for i in str(n):
        i = int(i)
        if i % 2 != 0:
            result *= i
    if result != 1:
        return result
    else:
        return 0
