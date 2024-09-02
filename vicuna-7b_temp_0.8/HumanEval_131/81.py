
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Handle special case of zero
    if n < 1:
        return 0
    # Handle special case of all digits being even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    # Otherwise, return the product of the odd digits
    return product(int(x) for x in str(n) if x % 2 != 0)