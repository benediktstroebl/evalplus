
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # if n is even, return 0
    if n % 2 == 0:
        return 0
    # if n has only one digit, return its digit value
    elif n < 10:
        return n
    # otherwise, divide n by 10, taking the modulus of the result
    else:
        return n // 10 + (n % 10 - 1) * (10 - 1) // 2
