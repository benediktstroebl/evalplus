
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    return_val = 1
    for i in str(n):
        i = int(i)
        if i % 2 != 0:
            return_val *= i
    if return_val == 1:
        return 0
    else:
        return return_val
