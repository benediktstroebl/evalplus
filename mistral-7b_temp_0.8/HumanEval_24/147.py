

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # since it is smaller than n, we can assume it is smaller than sqrt(n), to simplify the problem.
    upper_bound = int(n**0.5)
    for candidate in range(1, upper_bound+1):
        if n % candidate == 0:
            return candidate
    return upper_bound






