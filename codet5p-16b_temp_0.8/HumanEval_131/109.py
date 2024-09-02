
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
        digits_list.append(int(i))
    digits_product = 1
    for i in digits_list:
        if i % 2!= 0:
            digits_product = digits_product * i
    return digits_product




