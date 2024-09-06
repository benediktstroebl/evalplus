
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # check if all digits are even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    
    # otherwise, compute the product of the odd digits
    num = int(n)
    prod = 1
    for i in range(1, len(str(num))):
        if str(num)[i] % 2 == 1:
            prod *= num / 10
    return prod
