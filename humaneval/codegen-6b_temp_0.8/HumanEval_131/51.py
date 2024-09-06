
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits_sum = 0
    while n > 0:
        last_digit = n % 10
        if last_digit % 2 != 0:
            digits_sum = digits_sum + last_digit
        n = n // 10
    return digits_sum


