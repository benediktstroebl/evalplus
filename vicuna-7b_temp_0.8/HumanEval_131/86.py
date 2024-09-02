
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Return 0 if all digits are even
    if n%2 == 0:
        return 0

    # Calculate the product of the odd digits
    odd_digits = [n % d + 1 for d in range(10) if d % 2 != 0]
    return sum(odd_digits)