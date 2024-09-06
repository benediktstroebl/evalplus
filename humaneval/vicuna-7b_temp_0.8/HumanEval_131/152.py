
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = [int(d) for d in str(n)]
    while len(digits) > 0:
        remainder = 0
        for i in range(1, len(digits)):
            if (digits[i] % 2) != 0:
                remainder = digits[i] * remainder
                digits.remove(digits[i])
        n = remainder
    return n