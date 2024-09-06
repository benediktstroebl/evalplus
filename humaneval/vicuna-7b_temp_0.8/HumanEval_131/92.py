
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    # Otherwise, return the product of the odd digits
    return int(sum(map(lambda x: x % 2, str(n))))
