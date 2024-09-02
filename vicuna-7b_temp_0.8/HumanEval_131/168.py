
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # use binary search to find the middle index
    middle = len(str(n)) // 2
    result = 0
    for i in range(middle, len(str(n))):
        if n[i] % 2 != 0:
            result += n[i]
    return result
