
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # your code here
    n1 = str(n)
    res = 0
    for i in range(0, len(n1), 1):
        if int(n1[i]) % 2 != 0:
            res += int(n1[i])
    return res

