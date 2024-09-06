
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    result = 1

    if n < 10:
        return n

    while n > 9:
        digit = n % 10
        if digit % 2:
            result *= digit
        n /= 10

    if n % 2:
        result *= n

    return result
