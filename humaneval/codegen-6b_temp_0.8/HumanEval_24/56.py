

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # for i in range(1, n):
    #     if n % i == 0:
    #         k = i
    # return k
    import math

    r = int(n ** 0.5)
    # print(r)
    while r >= 1:
        # print(r)
        if n % r == 0:
            return r
        r -= 1

    return 1

