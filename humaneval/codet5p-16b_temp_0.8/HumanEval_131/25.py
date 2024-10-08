
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    result = 1
    for x in str(n):
        if int(x) % 2!= 0:
            result *= int(x)
        elif int(x) % 2 == 0 and int(x) == 0:
            result = 0
    return result
