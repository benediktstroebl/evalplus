

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check for even numbers that divide n evenly
    if n % 2 == 0:
        return 2

    # Check for odd numbers that divide n evenly
    while True:
        d = int(n // 2)
        if n % d == 0:
            return d

    return None
