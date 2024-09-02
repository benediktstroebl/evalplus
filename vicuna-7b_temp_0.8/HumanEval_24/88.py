

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [1, 2, 4, 8, 16, 32]
    while len(divisors) <= n:
        divisors.append(divisors[-1]**2)
    return divisors[-1]
