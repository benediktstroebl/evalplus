
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    # the logic: we need to keep the odd digits, so the first step is to convert the number into a list
    # then we can use list comprehension to extract the odd numbers, and the multiplication will be done in the comprehension
    # the final product is returned by the function

    number_list = list(str(n))
    product = 1
    for num in number_list:
        if int(num) % 2 == 0:
            continue
        else:
            product = product * int(num)
    return product
