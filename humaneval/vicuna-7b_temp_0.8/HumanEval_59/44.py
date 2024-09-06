

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Use trial division to find the smallest number of the form n - 2^i \* 3^j
    # that is greater than n.
    for i in range(1, 15):
        for j in range(1, 15):
            if (n - 2**i * 3**j) >= n:
                # If such a number is found, then it must be the largest prime factor.
                return n - 2**i * 3**j
    # If no such number is found, then the largest prime factor is n.
    return n
