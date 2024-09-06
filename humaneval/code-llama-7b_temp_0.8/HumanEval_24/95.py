

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    return largest_divisor_brute_force(n)
    # return largest_divisor_sieve(n)

