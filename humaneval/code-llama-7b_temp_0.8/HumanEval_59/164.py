

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # should be prime number, so need to skip 1 and 2
    # will loop through numbers and find the largest
    largest = 1
    for i in range(3, n, 2):
        if n % i == 0:
            largest = i
    return largest

