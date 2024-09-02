
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    
    mul = 1
    for i in str(n):
        if i % 2 == 0:
            mul = 0
            return mul
        else:
            mul *= int(i)
    return mul
    
    


















