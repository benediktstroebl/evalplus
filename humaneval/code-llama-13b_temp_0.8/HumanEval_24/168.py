

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # Search for the largest number that divides n evenly
    divisor = int(n / 2)
    while n % divisor != 0:
        divisor -= 1

    return divisor
