
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    "*** YOUR CODE HERE ***"
    even, odd = 1, 1
    s = str(n)
    for c in s:
        if int(c) % 2 == 0:
            even *= int(c)
        else:
            odd *= int(c)
    if even == 0:
        return 0
    return even * odd

