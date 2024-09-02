

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # largest_divisor can be written in terms of fractions.gcd
    #
    # from math import gcd
    # x, y = abs(n), abs(n)
    # while y:
    #     x, y = y, x % y
    # return x
    #
    # or
    #
    # n // 2**k * 2**(k - 1)
    # for k in range(1, int(n ** 0.5) + 1)[::-1]:
    #     if n % 2**k == 0:
    #         return 2**k
    #
    # 10 ** 9 * 2 ** 9
    # for n in reversed(range(10 ** 9 + 1)):
    #     if n % 10 == 9:
    #         return n // 10
    #
    # n ** 0.5
    #
    # n ** 0.5
    return n // 2
