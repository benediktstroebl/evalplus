

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Run through possible factors, starting with 2.
    # Whenever a divisor is found, remove it from the number.
    # At the end, the remaining number is the largest prime factor.
    largest = 0
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                largest = i
                n = n // i
                break
    return largest

