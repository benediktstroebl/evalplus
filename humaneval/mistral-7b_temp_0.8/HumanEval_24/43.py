

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # We start by determining the largest number that divides n evenly, smaller than n
    # We iterate through the range of possible divisors, starting from the largest possible divisor, and
    # decrementing until we find a divisor that divides n evenly
    # We then return the divisor that we found
    divisor = n
    while divisor > 1 and n % divisor != 0:
        divisor -= 1
    return divisor

