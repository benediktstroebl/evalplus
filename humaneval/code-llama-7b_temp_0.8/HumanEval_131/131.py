
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num_string = str(n)
    product = 1
    for char in num_string:
        int_char = int(char)
        if int_char % 2 == 1:
            product *= int_char
        else:
            product *= 0
    return product

