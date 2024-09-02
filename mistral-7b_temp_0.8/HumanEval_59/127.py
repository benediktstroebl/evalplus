

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Base case
    if n == 1:
        return 1

    # Loop until n is less than 2
    while n >= 2:
        # Divide n by smallest prime number until 0 remains
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                n = n // i
                break
        else:
            # If loop completes without a break, n is prime
            return n

    # If we reach here, we found the largest prime factor
    return n
