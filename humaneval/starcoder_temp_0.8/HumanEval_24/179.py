

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    k = 2
    while k * k <= n:
        while n % k == 0:
            n //= k
        k += 1
    return n
