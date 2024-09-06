
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    digits_list = []
    for d in str(n):
        if int(d) % 2!= 0:
            digits_list.append(int(d))
    if not digits_list:
        return 0
    else:
        return digits_list[0] * digits(digits_list[1:])

