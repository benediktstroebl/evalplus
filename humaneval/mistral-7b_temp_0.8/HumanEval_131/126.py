
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    result = 1
    a = str(n)
    for i in range(0,len(a)):
        if i % 2 == 1:
            result *= int(a[i])
    return result
