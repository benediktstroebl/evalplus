
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # a simple and naive approach: check if all digits are even
    # if so, return 0
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    
    # otherwise, return the product of the odd digits
    return sum(map(lambda x: int(x) if x % 2 == 1 else 0, str(n)))
