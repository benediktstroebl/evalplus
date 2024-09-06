
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # We use a list comprehension to create a list of the digits of n
    # and then use an if statement to check if any of the digits
    # are odd. If any of the digits are odd, we return the product
    # of those odd digits. If all of the digits are even, we return 0
    return [x for x in str(n) if x % 2 != 0] if [x % 2 != 0 for x in str(n)] else 0
