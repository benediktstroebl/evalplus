
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # n is positive
    assert n > 0

    # n has at least one digit that is odd
    if not any(digit > 0 for digit in n):
        return 0

    # convert n to a string for easier manipulation
    n = str(n)

    # reverse the string
    n = n[::-1]

    # remove all leading zeros
    n = '0' * len(n)

    # split the string into a list of digits
    digits = [int(digit) for digit in n]

    # return the product of the odd digits
    return sum(digits[i] * (i % 2 == 1) for i in range(len(digits)))
