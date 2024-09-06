

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Create a list of the first ten primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # If n is less than the first prime (2), the largest prime factor is 1
    if n < primes[0]:
        return 1
    # Loop through the primes list and check if any are prime factors
    for prime in primes:
        # If n is divisible by the prime, the prime is the largest prime factor
        if n % prime == 0:
            return prime
    # If n is not divisible by any of the primes, the largest prime factor is n
    return n

