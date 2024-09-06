
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # base case: if all digits are 0 or 1, return the product
    if n < 10:
        return n

    # find the largest digit greater than 1
    digit = max(n//i + 1 for i in range(len(str(n)) - 1))

    # initialize the product to 1
    product = 1

    # loop through the digits
    for i in range(len(str(n)) - 1):
        # if the current digit is odd, multiply the product by i and add 1
        product *= i + 1

    # return the product
    return product
