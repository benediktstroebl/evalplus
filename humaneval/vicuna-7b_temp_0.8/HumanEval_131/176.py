
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # The product of the digits is simply the sum of the digits
    product = n // (10 ** len(str(n)))
    # Check if all digits are odd
    if product % 2 == 0:
        return 0
    # The odd digits are the last digits
    last_digits = str(n)[-1::-1]
    # Multiply the last digits by the product of the digits
    return product * last_digits
