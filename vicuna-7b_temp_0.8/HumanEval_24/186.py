

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [2, 4, 6, 8, 10, 12, 14, 15]
    for divisor in divisors:
        if n % divisor == 0:
            return max(divisors, n // divisor + 1)
    return 15
