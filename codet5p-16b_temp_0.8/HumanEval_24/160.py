

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    
    divisors = list(filter(lambda x: n % x == 0, range(1, int(n ** 0.5) + 1)))
    return max(divisors) if len(divisors) > 0 else n

