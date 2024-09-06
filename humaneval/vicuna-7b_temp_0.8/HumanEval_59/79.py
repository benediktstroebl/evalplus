

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        raise ValueError(f"{n} is too small")
    if n % 2 == 0:
        return n / 2
    while n > 3:
        if n % 3 == 0:
            return n / 3
        n = n - 3
    while n > 5:
        if n % 5 == 0:
            return n / 5
        n = n - 5
    while n > 7:
        if n % 7 == 0:
            return n / 7
        n = n - 7
    while n > 11:
        if n % 11 == 0:
            return n / 11
        n = n - 11
    if n > 121:
        # use the Miller-Rabin primality test
        for _ in range(80):
            a = random.randint(2, int(n**0.5) - 2)
            b = random.randint(2, int(n**0.5) + 2)
            if gcd(a, b) == 1 and \
               is_prime(a) and \
               is_prime(b) and \
               a != b and \
               any(pow(a, d, b) == 1 for d in range(2, int(sqrt(n)) + 1)):
                return a
        raise ValueError(f"{n} is not prime")
    # if we get here, n is prime
    return n
