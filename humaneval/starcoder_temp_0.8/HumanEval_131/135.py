
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    # YOUR CODE HERE
    s = 1
    for x in n:
        if x%2 == 1:
            s*=x
    return s
