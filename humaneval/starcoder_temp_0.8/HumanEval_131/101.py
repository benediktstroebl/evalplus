
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Only positive integers
    if n < 0:
        return 0
    # If n is 0 or 1
    elif n <= 1:
        return n
    # If all numbers are even
    elif n % 2 == 0:
        return 0
    else:
        return digits(n // 10) * (n % 10)

