
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # make copy of n
    num = n
    product = 1
    # while we have digits
    while(num > 0):
        # get last digit
        digit = num % 10
        # if last digit is odd
        if digit % 2 == 1:
            # multiply by original
            product *= digit
        # update number
        num /= 10
    return product
