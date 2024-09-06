
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # ALGORITHM:
    # the product of all the digits is the product of odd numbers index-by-index
    # by separating into groups of consecutive numbers, and multiplying them
    # together. To do this, we use a variable to keep track of the product,
    # and that product will be multiplied by the value of the digit.
    #
    # Approach:
    # add tests to check the base case (all evens), and the edge case (single digit)
    # write algorithm to think through the base case...
    nstr = str(n)
    prod = 1
    if len(nstr) == 1:
        return int(nstr)
    for i in range(1,len(nstr),2):
        i = int(nstr[i])
        if i % 2 != 0:
            prod *= i
    return prod
