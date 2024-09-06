
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n % 2 != 0:
        return n // 2
    else:
        for i in range(1, len(str(n))):
            if str(n)[:i] == str(n)[i+1:] % 2 == 1:
                return n // 2
        return 0
