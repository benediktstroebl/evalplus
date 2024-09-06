
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if (n % 2 == 0):
        return 0
    # Check if the last digit is odd
    last_digit = n % 10
    if last_digit == 1:
        return 10 * digits(n // 10)
    # Check if the second-last digit is odd
    second_last_digit = n // 10 % 10
    if second_last_digit == 1:
        return 10 * digits(n // 100) + digits(n // 10)
    # Otherwise, return 0
    return 0
