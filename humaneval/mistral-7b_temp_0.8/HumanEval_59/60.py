

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # TODO: Implement largest_prime_factor.
    # If n = 1, return 1
    if n == 1:
        return 1
    # Get all the factors of n
    factors = [i for i in range(2, n + 1) if n % i == 0]
    # Get the largest factor
    largest_factor = max(factors)
    # If largest_factor is prime, return largest_factor
    if is_prime(largest_factor):
        return largest_factor
    # Return the largest_prime_factor of largest_factor
    else:
        return largest_prime_factor(largest_factor)

