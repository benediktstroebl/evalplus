

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return max(factors, key=lambda x: n // x)