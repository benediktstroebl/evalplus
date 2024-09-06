

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_divisor_n = n
    for divisor in range(2, int(n**0.5)):
        if n % divisor == 0:
            largest_divisor_n = divisor
    return largest_divisor
