
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    p = 1
    for digit in str(n):
        n = int(digit)
        if n % 2 == 0:
            continue
        p *= n
    return p

