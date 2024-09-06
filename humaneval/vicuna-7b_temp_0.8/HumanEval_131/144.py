
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Time: O(n)
    # Space: O(1)
    if n < 1:
        return 0
    while n > 1:
        n = n // 2
        if n % 2 == 0:
            n = 0
        else:
            n += 1
    return n
