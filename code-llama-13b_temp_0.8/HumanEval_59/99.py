

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    """
    1. largest prime factor will be prime
    2. can use a while loop to keep dividing n by prime factors
    3. increment n while prime factors are still factors of n
    """
    prime = 2
    while n % prime != 0:
        prime += 1
    return prime
