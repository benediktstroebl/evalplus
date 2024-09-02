
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 10:
        if n % 2 == 1:
            return n
        else:
            return 0
    else:
        n = str(n)
        n = int(n[1:])
        n = int(n[0])*int(n[1])*int(n[2])
        return n
