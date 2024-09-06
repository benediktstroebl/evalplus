

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Edge case, for powers of two
    if n & (n - 1) == 0:
        return n

    largest_prime = 1
    # Start with smallest prime and work up
    for i in range(2, n + 1):
        # Ensure we don't divide by an even number
        if i % 2 != 0:
            if n % i == 0:
                largest_prime = i
                # Reassign n to make division easier
                n = n // i
                # If after dividing, the number is prime, stop
                if n == 1:
                    break
    return largest_prime
