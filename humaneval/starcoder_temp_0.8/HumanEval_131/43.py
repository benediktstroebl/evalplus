
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    assert n >= 0 and int(n) == n, "n is not a positive integer"
    digits = []
    while n!= 0:
        digits.append(n % 10)
        n = n // 10
    prod = 1
    for x in digits:
        if x % 2 == 1:
            prod *= x
    return prod
