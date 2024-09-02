

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    largest_prime_factor = None

    while n > 1:
        if n % 2 == 0:
            n /= 2
            largest_prime_factor = 2
        else:
            for i in range(3, n + 1):
                if n % i == 0:
                    n /= i
                    largest_prime_factor = i
                    break

    return largest_prime_factor

