

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while True:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return i
        n -= 1
    return n
