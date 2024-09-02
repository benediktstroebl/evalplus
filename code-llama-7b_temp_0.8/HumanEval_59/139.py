

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Get prime factors of n, and store as a set.
    prime_factors = set()
    # 2 is the only even prime, so test for it first.
    # If n is even, divide n by 2 and keep going.
    while n % 2 == 0:
        prime_factors.add(2)
        n //= 2

    # If n is now 1, we are done.
    if n == 1:
        return max(prime_factors)

    # Now test the odd numbers from 3 to sqrt(n).
    i = 3
    while i <= n:
        # If n is divisible by i, add i to the set of prime factors.
        while n % i == 0:
            prime_factors.add(i)
            n //= i
        # Advance to the next odd number.
        i += 2

    # If n is now 1, we are done.
    if n == 1:
        return max(prime_factors)

    # Otherwise, n is a prime itself, so return it.
    return n

