

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Find divisors
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    # Find largest number smaller than n
    largest_divisor = max([i for i in divisors if i < n])
    return largest_divisor

