
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Add.  This is the number of digits in the sum.
    d = 0
    while n > 0:
        d += n % 10
        n = n // 10
    # Multiply.  This is the product of the odd digits.
    p = 1
    for i in range(d+1):
        p *= (d % 10 == 1)
        d //= 10
    return p
