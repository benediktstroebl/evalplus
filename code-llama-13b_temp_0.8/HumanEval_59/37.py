

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # largest prime factor greater than one
    if n % 2 == 0:
        return 2

    for i in range(3, n, 2):
        if n % i == 0:
            return i

    # print(largest_prime_factor(13195))
    # print(largest_prime_factor(600851475143))

    return n

