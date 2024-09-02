

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check all numbers up to the square root of n
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return None
