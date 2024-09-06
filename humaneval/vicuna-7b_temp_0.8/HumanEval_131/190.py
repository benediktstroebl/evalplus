
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
    # Iterate through the digits of n, starting from the right
    for i, c in enumerate(str(n)[::-1]):
        # If the current digit is odd, add its product to the result
        if c % 2 != 0:
            result += c
    return result
