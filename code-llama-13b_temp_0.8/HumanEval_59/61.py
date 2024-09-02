

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # METHOD 1: Brute force
    # i = 2
    # while i * i <= n:
    #     if n % i == 0:
    #         return i
    #     i += 1
    # return n

    # METHOD 2: Smarter brute force
    # Note that we can terminate the loop early: i * i <= n is equivalent to i <= sqrt(n)
    # i = 2
    # while i * i <= n:
    #     if n % i == 0:
    #         return i
    #     i += 1
    # return n

    # METHOD 3: Fermat's Theorem
    # Fermat's Little Theorem: a^(p - 1) = 1 (mod p), for any a and p prime.
    # Therefore, a^(p - 2) = a^(p - 1) * a = 1 (mod p) => ap = 1 (mod p) => p | ap - 1
    # We want to find the largest prime factor of n, so we try all primes that divide n.
    # In other words, we do long division with each prime that divides n, starting with 2.
    from math import sqrt
    i = 2
    while i * i <= n:
        if n % i == 0:
            # We've found a factor, now we want to find the largest factor among
            # 2 * 2 * 2 * 2 * ... * 2 and 3 * 3 * ... * 3
            # so we do the following division as long as the result is evenly divisible by i
            while n % i == 0:
                n //= i
        i += 1
    return n

