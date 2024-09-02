
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # the first digit is the biggest odd number, and we can multiply it
    # by 10 to get a large number
    return (10**len(str(n)) // n) % 10
