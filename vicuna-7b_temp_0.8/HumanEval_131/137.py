
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Handle the case when all digits are even
    if all(c in "04689" for c in str(n)):
        return 0

    # Initialize a variable d to store the product of the odd digits
    d = 1

    # Loop through the digits of n and multiply them together
    for digit in str(n)[2:]:
        d *= digit

    return d
