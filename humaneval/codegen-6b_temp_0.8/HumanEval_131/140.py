
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
    n = str(n)
    total = 1
    for i in range(len(n)):
        if (i + 1) % 2 == 1:
            total *= int(n[i])
    return total
