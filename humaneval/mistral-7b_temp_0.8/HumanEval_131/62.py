
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    #I have used a temporary list for the purpose of this exercise
    num = list(str(n))
    total = 1
    for i in num:
        if int(i) % 2 != 0:
            total *= int(i)
    return total
