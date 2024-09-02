
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 0
    else:
        result = 1
        for i in range(len(str(n))-1, -1, -1):
            x = int(str(n)[i])
            if x % 2 != 0:
                result *= x
        return result
