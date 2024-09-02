
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
        # Check if the last digit is even
        if n % 2 == 0:
            n //= 10
            continue
        # Multiply the product by the digit
        product *= (n % 10)
        n //= 10
    return product

