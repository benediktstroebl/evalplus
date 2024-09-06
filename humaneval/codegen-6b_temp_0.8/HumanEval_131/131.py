
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # single digit numbers are easy
    if n < 10:
        return n

    # split by every other digit
    z = []
    while n:
        z.append(n % 10)
        n = n // 10

    # list of odds
    n = []
    for i in range(0, len(z), 2):
        n.append(z[i])

    # product of odds
    p = 1
    for i in range(len(n)):
        p *= n[i]

    return p

