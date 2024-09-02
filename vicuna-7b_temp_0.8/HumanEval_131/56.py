
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # If the number is even, return 0
    if n % 2 == 0:
        return 0

    # Otherwise, calculate the product of the odd digits
    # and return it
    digits = [int(n) % 10]
    while digits[-1] % 2 == 0:
        digits.pop()
    return digits[0] * 10 ** len(digits)
