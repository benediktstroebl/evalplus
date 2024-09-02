

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        raise ValueError("Input must be at least 2")
    for i in range(n, 0, -1):
        if n % i == 0:
            return i
    raise ValueError("Largest divisor not found")
