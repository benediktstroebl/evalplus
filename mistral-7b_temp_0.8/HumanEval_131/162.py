
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # return my_product(filter(lambda x: x % 2 == 1, my_list(n)))
    return my_product(filter(lambda x: x % 2 != 0, my_list(n)))

