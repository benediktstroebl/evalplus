
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    s = str(n)
    return sum(int(s[i]) for i in range(len(s)) if i % 2 == 1)

