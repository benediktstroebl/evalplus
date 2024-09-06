
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # check for cases where all digits are even or all digits are odd
    if sum(i % 2 == 0 for i in str(n)) == len(str(n)):
        return 0
    else:
        # use a loop to iterate through the digits and multiply them together
        product = 1
        for i in str(n):
            if i % 2 != 0:
                product *= i
        return product
