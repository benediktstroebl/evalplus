
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    else:
        prod = 1
        while n > 0:
            digit = n % 10
            if digit % 2 == 1:
                prod *= digit
            n = n // 10
        return prod

