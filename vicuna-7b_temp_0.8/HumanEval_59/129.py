

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # n is not a prime, so we can use the Sieve of Eratosthenes
    # algorithm to find the prime factors of n
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            # if n is divisible by p, then there are no prime factors
            # greater than p
            break
    else:
        # if n is not divisible by any prime less than n**0.5,
        # then the largest prime factor of n is n itself
        return n

    # n is divisible by a prime less than n**0.5, so we can find
    # the largest prime factor by finding the first prime greater
    # than n**0.5 and using it as the largest prime factor
    for i in range(int(n**0.5) + 1):
        if n % i == 0:
            # if n is divisible by i, then there are no prime factors
            # greater than i
            break
    else:
        # if n is not divisible by any prime less than n**0.5,
        # then the largest prime factor of n is the first prime greater
        # than n**0.5
        return i
