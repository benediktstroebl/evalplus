
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    def isEven(num):
        return num % 2 == 0

    res = []

    if n == 0:
        return 0

    while n > 0:
        rem = n % 10
        n = n // 10
        if rem % 2 == 1:
            res.append(rem)

    if len(res) == 0:
        return 0

    res.sort()
    return reduce(lambda x,y: x*y, res)
