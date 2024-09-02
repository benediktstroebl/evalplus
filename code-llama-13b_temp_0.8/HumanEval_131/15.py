
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 10:
        return n
    num = str(n)
    prod = 1
    for i in range(0, len(num)):
        if (int(num[i]) % 2) != 0:
            prod = prod * int(num[i])
    return prod
    
    
