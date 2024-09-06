
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 10:
        return 0
    else:
        digits = str(n)
        count = 0
        for i in digits:
            if int(i) % 2 != 0:
                count = count * int(i)
        return count
