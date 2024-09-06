
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 0:
        return 0
    num = n
    if (n % 2 == 0):
        return 0
    else:
        while num > 0:
            if (num % 10) % 2 == 1:
                return num % 10
            num = num // 10
