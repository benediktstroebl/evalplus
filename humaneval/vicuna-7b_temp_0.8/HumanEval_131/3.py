
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = [int(n) % 10 for n in range(10)]
    for i in range(1, len(digits)):
        if digits[i] % 2 != digits[i - 1] % 2:
            return digits[i]
    return 0
