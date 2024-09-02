

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2
    # at this point n is either a prime or a composite whose prime factors are
    # greater than 2
    if is_prime(n):
        prime_factors.append(n)
    else:
        # we now have a composite who's prime factors are all greater than 2.
        # We can therefore divide by all of them without leaving a remainder.
        # We can also stop when we reach the square root of n
        for possible_factor in range(3, int(n ** 0.5) + 1, 2):
            if n % possible_factor == 0:
                prime_factors.append(possible_factor)
                n = n // possible_factor
        # we may have left a remainder
        if n > 2:
            prime_factors.append(n)
    return max(prime_factors)

