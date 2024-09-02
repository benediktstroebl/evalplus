

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_list = []
    largest_prime_factor = 1
    if n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                if i > largest_prime_factor:
                    largest_prime_factor = i

    return largest_prime_factor

