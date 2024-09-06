
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digit_string = str(n)
    for char in digit_string:
        if char in '0123456789':
            digit_string = digit_string.replace(char, '')
        else:
            return 0
    return int(digit_string)

