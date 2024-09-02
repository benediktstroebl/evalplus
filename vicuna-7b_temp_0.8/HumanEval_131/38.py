
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use a variable 'x' to accumulate the product of the digits
    # The product of 10n + x starts with 10*x + 1 = 1 and is equal to 10^n
    x = 1
    for i in range(n-1, -1, -1):
        x *= 10
        x += (n % 10) * (n // 10)
    if (n % 2 == 0):
        return 0
    return x
