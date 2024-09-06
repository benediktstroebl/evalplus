
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = int(n)
    if n < 0 or not n % 10 in {0, 3, 5, 7, 9}:
        return 0
    digits = []
    for i in range(n, 0, 10):
        if i % 2 == 0:
            digits.append(0)
        else:
            digits.append(i)
    return sum(digits)
