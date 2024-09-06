
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    return_num = 0
    for num in str(n):
        if int(num) % 2 != 0:
            return_num *= int(num)
    return return_num
