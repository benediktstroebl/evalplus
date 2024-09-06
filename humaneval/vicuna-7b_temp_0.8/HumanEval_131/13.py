
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = 0
    for i in range(n):
        if n % i == 0:
            digits = digits * 10 + int(n // i)
            n = n // i
            break
    return digits
