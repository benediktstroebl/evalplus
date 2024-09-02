
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    i = 1
    res = 1
    while n > 9:
        for digit in str(n):
            if int(digit) % 2!= 0:
                res *= int(digit)
        n = res
        res = 1
        i += 1
    if i == 1:
        return n
    else:
        return 0
