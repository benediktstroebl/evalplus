
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if all(d % 2 == 0 for d in str(n)):
        return 0
    # Calculate the product of the odd digits
    odd_digits = [d % 2 != 0 for d in str(n)]
    return sum(1 for d in odd_digits if d % 2 == 1)