

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    for possible_factor in range(n, 1, -1):
        if n % possible_factor == 0:
            is_prime = True
            for num in range(2, possible_factor):
                if possible_factor % num == 0:
                    is_prime = False
                    break
            if is_prime:
                return possible_factor

