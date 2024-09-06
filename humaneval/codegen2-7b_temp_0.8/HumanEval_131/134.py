
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n <= 0:
        return 0
    n = str(n)
    count = 0
    for i in range(len(n)):
        if n[i] % 2 == 1:
            count += int(n[i])
    return
