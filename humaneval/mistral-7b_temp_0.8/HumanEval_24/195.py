

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 0:
        raise ValueError("Input should be positive")
    for i in range(1, n + 1):
        if n % i == 0:
            if i > n // i:
                return i
    return n

