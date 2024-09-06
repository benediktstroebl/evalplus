
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 10:
        return n
    else:
        next_n = n % 10
        rest_n = n // 10
        if next_n % 2 != 0:
            return next_n * digits(rest_n)
        else:
            return digits(rest_n)













