
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    result = 1
    string = str(n)
    for char in string:
        int_char = int(char)
        if int_char % 2 == 0:
            pass
        else:
            result *= int_char
    return result
