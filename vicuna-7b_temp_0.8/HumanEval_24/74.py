

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Find all the factors of n
    factors = [1]
    for i in range(1, n + 1):
        while i % i == 0:
            factors.append(i)
        # Find the largest factor smaller than n
        largest_factor = min(factors, key=lambda x: x if n % x == 0 else x - 1)
    return largest_factor
