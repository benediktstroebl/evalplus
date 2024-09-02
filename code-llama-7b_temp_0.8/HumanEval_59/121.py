

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    max_prime = 2

    # We can loop through all odd numbers starting at 3, as even numbers are not prime.
    for prime in range(3, n + 1, 2):
        is_prime = True

        # We need to loop through all numbers that are not prime until we find one that isn't divisible.
        for num in range(2, prime):
            if prime % num == 0:
                is_prime = False
                break
        if is_prime:
            if max_prime < prime:
                max_prime = prime

    return max_prime

