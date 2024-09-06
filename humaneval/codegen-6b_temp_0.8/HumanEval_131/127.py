
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    ans = 1 # A list of the digits, starting with 1
    for d in n:
        if int(d) % 2:
            ans *= d
    return ans
