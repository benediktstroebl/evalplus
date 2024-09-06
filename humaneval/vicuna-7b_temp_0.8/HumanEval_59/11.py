

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # If n is prime, return n as the largest prime factor.
    if n > 1 and n % 2 == 0:
        return n

    # Try a few small values of n to see if they are prime.
    if n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 5:
        return 5

    # Use the Sieve of Eratosthenes to find all prime numbers less than sqrt(n).
    prime_indices = [i for i in range(len(range(sqrt(n)) + 1) // 2) if n % 2**i == 0]

    # If there are any prime factors, return the largest of them.
    for p in prime_indices:
        if n % p == 1:
            return p

    # If no prime factors are found, return n.
    return n
