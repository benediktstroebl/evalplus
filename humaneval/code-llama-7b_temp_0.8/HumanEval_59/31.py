

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    for i in range(3, n + 1):
        # Test if i divides n without remainder
        if n % i == 0:
            # Test if i is prime
            for j in range(2, i):
                if i % j == 0:
                    break
            # i is prime
            else:
                return i
    return 1

