

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Define a list of prime numbers up to the square root of n.
    primes = [p for p in range(2, int(n ** 0.5) + 1) if p % 2 == 1]
    # Initialize a variable to store the largest prime factor.
    largest_prime = 2
    # Iterate through the list of primes.
    for p in primes:
        if p >= n:
            # If p is greater than or equal to n, it is not a prime.
            break
        # If p is a prime, update the largest prime.
        if p > largest_prime:
            largest_prime = p
    return largest_prime
