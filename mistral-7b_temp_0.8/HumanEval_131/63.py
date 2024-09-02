
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    x = str(n)
    odd_d = 0
    for i in range(0, len(x)):
        if i%2 == 1:
            odd_d += int(x[i])
    return odd_d
