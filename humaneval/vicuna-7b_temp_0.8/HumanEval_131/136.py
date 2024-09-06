
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use a negative loop variable to check for odd digits
    for i in range(len(str(n))):
        if n % 2 != 0:
            return n
    return 0