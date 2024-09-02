
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # returns the product of the odd digits

    # make a string of all the digits
    digits_str = str(n)

    # initialize the product to 1
    product = 1

    for digit in digits_str:
        # if the digit is even, skip it
        if int(digit) % 2 == 0:
            continue
        # otherwise, multiply the product by the current digit
        product *= int(digit)

    # return the product
    return product

