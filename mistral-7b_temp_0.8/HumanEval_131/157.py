
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    sum = 1
    for i in str(n):
        if i % 2 == 1:
            sum *= int(i)
    if sum == 1:
        return 0
    else:
        return sum


