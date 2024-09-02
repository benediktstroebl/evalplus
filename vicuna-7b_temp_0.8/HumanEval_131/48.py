
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Find all the digits of n, and get a list of odd numbers
    digits = [x for x in str(n) if x % 2 == 1]
    if not digits:
        return 0
    # Multiply the odd digits and return the result
    return reduce(mul, digits, 1)
