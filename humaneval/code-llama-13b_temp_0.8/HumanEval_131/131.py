
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    return_val = 1
    for number in str(n):
        if int(number) % 2 != 0:
            return_val *= int(number)
    if return_val == 1:
        return 0
    return return_val

