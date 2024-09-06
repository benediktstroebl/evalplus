def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1) == 1
    digits(4) == 0
    digits(235) == 15
    """
    if not isinstance(n, int) or n < 0:
        return "Input must be a positive integer"
    product = 1
    for digit in str(n):
        if int(digit) % 2:  # If the digit is odd
            product *= int(digit)  # multiply the current digit to the product
    return product