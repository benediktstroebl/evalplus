
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
    
    # if not all digits are even, return the product of the odd digits
    else:
        return int(sum(map(lambda x: x * (x % 2) // 2, str(n))))
