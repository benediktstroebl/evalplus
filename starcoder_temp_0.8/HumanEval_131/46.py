
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if n == 0:
        return 0

    if n < 0:
        return 0

    if n < 10:
        if n % 2 == 0:
            return 0
        else:
            return n

    # if n >= 10
    # return n * digits(n // 10)

    # if n is even
    # 2325 -> 232 -> 2
    # 23 -> 23

    # if n is odd
    # 2325 -> 232 -> 25
    # 23 -> 23

    # 2325 -> 232 -> 2, 25
    # 25 / 2 -> 12.5 -> 12
    # 12 / 2 -> 6
    # 2 * 6 -> 12
    # return 2 * digits(n // 10)

    return n % 10 * digits(n // 10)
