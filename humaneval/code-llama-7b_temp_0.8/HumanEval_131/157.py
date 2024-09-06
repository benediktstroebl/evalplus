
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Assign the number to a string.
    n = str(n)

    # Create an empty list and then populate it with the odd digits.
    # Initialize the product to 1 because we're multiplying odd digits.
    # If there are no odd digits, then the list is empty and we'll return 0.
    product = 1
    digits = []

    for digit in n:
        if int(digit) % 2 == 1:
            digits.append(digit)

    for digit in digits:
        product *= int(digit)

    return product
