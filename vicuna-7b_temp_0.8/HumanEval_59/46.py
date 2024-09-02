

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # check if n is prime
    if n > 1 and n % 2 == 0:
        return 2
    # check if n is even
    if n % 2 == 0:
        return 3
    # try to find the largest prime factor
    factors = []
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            break
        factors.append(i)
    # find the largest prime factor in the list
    largest = max(factors)
    # try to find the largest prime factor again
    factors = []
    for i in range(2, largest + 1, 2):
        if largest % i == 0:
            break
        factors.append(i)
    # find the largest prime factor in the list
    largest = max(factors)
    return largest
