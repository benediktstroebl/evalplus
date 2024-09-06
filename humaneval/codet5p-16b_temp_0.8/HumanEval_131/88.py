
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    digits_list = []
    for i in str(n):
        if int(i) % 2!= 0:
            digits_list.append(int(i))
    if len(digits_list) == 0:
        return 0
    else:
        return reduce(lambda x,y: x*y, digits_list)
