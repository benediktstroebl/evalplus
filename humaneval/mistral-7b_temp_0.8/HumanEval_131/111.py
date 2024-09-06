
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    oddDigits = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        while n > 0:
            if n % 10 % 2 == 1:
                oddDigits.append(n % 10)
            n = n // 10
        return reduce(lambda x,y: x*y,oddDigits)


























































































































































