
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # check for even number
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    # check for number greater than 1
    if n < 1:
        return 0
    # get the odd digits and multiply
    digits = [int(d) for d in str(n)[1:]]
    product = 1
    for i in range(len(digits) - 1):
        product *= digits[i]
    return product
