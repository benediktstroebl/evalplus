

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Following the pseudocode at https://en.wikipedia.org/wiki/Primality_test#Pseudocode:_Trial_division

    # Check if n is even.
    if n % 2 == 0:
        return 2

    # Search for prime factors up to the sqrt of n.
    largest_factor = 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            largest_factor = i

    return largest_factor

