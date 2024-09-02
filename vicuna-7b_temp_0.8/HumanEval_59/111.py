

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Use trial division to check if n is a prime
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return 0
        return n
    else:
        # n is not a prime, so find its largest prime factor
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                # If n is divisible by a number that is not prime,
                # it must have a smaller prime factor, so return that
                return i
        return 1