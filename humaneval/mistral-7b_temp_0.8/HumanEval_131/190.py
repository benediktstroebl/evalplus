
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num_string = str(n)
    digits = []
    for digit in num_string:
        if int(digit) % 2 != 0:
            digits.append(int(digit))
    return sum(digits)
