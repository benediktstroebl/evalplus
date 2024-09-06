

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # If n is a prime, return n.
    if n > 1 and n % 2 == 0:
        return n

    # If n is less than 3, it is certainly composite, so we return 2.
    if n < 3:
        return 2

    # Otherwise, we find the largest prime factor of n by repeatedly
    # dividing n by the prime numbers in the range (2, sqrt(n)).
    # If n is divisible by a prime in this range, we know that it is not
    # divisible by any smaller prime, so we can stop. Otherwise, we
    # continue the search until we find a prime that divides n.

    # We use a list to store the prime numbers in the range (2, sqrt(n)).
    primes = [p for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31) if n % p == 0]

    # If the list is empty, n is certainly composite.
    if not primes:
        return 2

    # Otherwise, we start by considering the first prime in the list.
    p = primes[0]

    # We repeat the following loop until we find the largest prime factor
    # of n or we run out of primes in the list.
    for i in range(1, len(primes)):
        # If n is divisible by p, we know that it is not divisible by any
        # smaller prime in the list, so we can stop.
        if n % p == 0:
            return p

        # Otherwise, we continue the loop, using p as the next prime to
        # consider.
        p = primes[i]

    # If we run out of primes in the list, n is certainly composite.
    # In this case, we return 2 as the largest prime factor.
    return 2
