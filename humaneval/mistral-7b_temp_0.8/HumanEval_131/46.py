
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # return product of digits
    # return 0 if all digits are even
    # convert to string
    # 1234 => ['1', '2', '3', '4']
    digits_list = list(str(n))

    # product of odd digits
    product = 1

    # check if all are even
    for i in digits_list:
        if int(i) % 2 != 0:
            product *= int(i)

    if product == 0:
        return 0
    return product
