
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    total = 0
    for char in str(n):
        if int(char) % 2!= 0:
            total *= int(char)
    return total
