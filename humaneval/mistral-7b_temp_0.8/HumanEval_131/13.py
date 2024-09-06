
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        my_list = [x for x in str(n)]
        my_list = [int(x) for x in my_list]
        my_list = [y for y in my_list if y % 2 == 1]
        my_list = list(map(lambda x: x*x, my_list))
        return sum(my_list)
