
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    my_product = 1
    my_list = []
    my_list[:0] = str(n)
    for x in my_list:
        x = int(x)
        if x % 2 != 0:
            my_product *= x
        else:
            my_product = 0
    return my_product
