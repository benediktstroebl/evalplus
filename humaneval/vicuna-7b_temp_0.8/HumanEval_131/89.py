
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # check if all digits are even
    if sum(map(lambda x: x % 2, n)) == 0:
        return 0
    
    # compute the product of the odd digits
    digits = [int(n % d) for d in range(10)]
    prod = 1
    for d in digits:
        prod *= d
    return prod
