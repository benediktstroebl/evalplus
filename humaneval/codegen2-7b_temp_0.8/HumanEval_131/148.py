
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    even_digits = 0
    for d in str(n):
        if d!= '0':
            even_digits += int(d)
    return even_digits

