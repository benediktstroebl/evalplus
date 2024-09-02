

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    divisors = [d for d in range(2, int(n**0.5)+1) if n % d == 0]
    return max(divisors, default=1)

