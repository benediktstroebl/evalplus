
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if n == 0:
        return 0
    else:
        digits = [int(digit) for digit in str(n)]
        odd_digits = [digit for digit in digits if digit % 2 == 1]
        return multiply(odd_digits)

