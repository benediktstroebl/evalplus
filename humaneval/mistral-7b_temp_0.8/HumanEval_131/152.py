
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    num = str(n)
    odd = 1
    for i in num:
        if int(i)%2 != 0:
            odd *= int(i)
        if len(num) == 0:
            return 0
    return odd
