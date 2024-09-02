
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    result = 1
    while n > 0:
        last = n % 10
        if last % 2 == 0:
            return 0
        else:
            result *= last
            n = (n - last) // 10
    return result

