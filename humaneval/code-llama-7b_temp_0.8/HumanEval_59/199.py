

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # print("Starting factoring...")
    # Initialize the largest prime factor to 1.
    largest = 1
    i = 2
    while i ** 2 <= n:
        while n % i == 0:
            largest = i
            n = n // i
        i += 1
    if largest == 1:
        largest = n
    return largest
