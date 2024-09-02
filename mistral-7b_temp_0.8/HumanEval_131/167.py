
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    # Convert n to a string.
    n = str(n)

    # Check if all digits are even.
    even_digits = True
    for digit in n:
        if digit % 2 == 1:
            even_digits = False
    if even_digits:
        return 0

    # Return the product of odd digits.
    product = 1
    for digit in n:
        if digit % 2 == 1:
            product *= int(digit)
    return product
