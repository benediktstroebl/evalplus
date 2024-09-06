

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while True:
        divisor = 2 * max(int(n/divisor) for divisor in range(2, n + 1))
        if divisor <= n:
            break
    return divisor
