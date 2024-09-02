

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = get_divisors(n)
    return max(divisors, key=lambda x: abs(n-x))
