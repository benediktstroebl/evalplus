
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    import math

    if n == 1:
        return n
    else:
        ans = 1
        while n > 1:
            digit = n % 10
            ans = ans * digit
            n = int(math.fabs(n) / 10)
        return ans

