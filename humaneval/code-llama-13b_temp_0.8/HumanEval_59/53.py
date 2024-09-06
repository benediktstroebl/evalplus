

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # This prime number to check.
    prime = 3

    # Check the number divided by the prime.
    # If not evenly divided, check the next prime.
    # Otherwise, divide the number by this prime.
    # Continue until the prime is greater than the number.
    while n % prime != 0:
        prime += 2

    return prime

