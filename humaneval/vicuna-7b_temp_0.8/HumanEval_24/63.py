

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check all prime numbers less than n
    for p in prime_numbers(n):
        if n % p == 0:
            return p
    
    # If no divisor was found, return the largest prime number up to n
    # but not greater than n
    return max(prime_numbers(n), key=lambda x: x if x > n else x)
