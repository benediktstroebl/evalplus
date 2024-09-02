
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Make sure the number is not negative.
    if n < 0:
        return 0

    # Initialize the product to 1.
    product = 1

    # Iterate over the digits of the number.
    while n > 0:
        # Get the last digit of the number.
        digit = n % 10

        # If the digit is odd, multiply it to the product.
        if digit % 2 == 1:
            product *= digit

        # Divide the number by 10 to remove the last digit.
        n //= 10

    return product

