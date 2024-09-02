

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n == 2:
        return n

    max_prime = n

    if n % 2 == 0:
        max_prime = 2

        while n % 2 == 0:
            n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            max_prime = i

            while n % i == 0:
                n //= i

    if n > 2:
        return n

    return max_prime


