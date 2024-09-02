
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    L = []
    while n > 0:
        L.append(n % 10)
        n = n // 10
    return prod([x for x in L if x % 2 == 1])


