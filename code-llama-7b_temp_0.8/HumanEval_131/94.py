
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1

    while n > 0:
        # Get the last digit
        digit = n % 10
        # If it's odd, multiply it by the product
        if digit % 2 == 1:
            product *= digit
        # Remove the last digit from n and repeat
        n = n // 10

    return product

