

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # 2 is the only even number that is prime
    if n % 2 == 0:
        return 2

    # range goes up to the square root of n
    # i.e. the largest number that n can be divided by
    for i in range(3, int(n**0.5)+1, 2):
        # Checks if i divides n
        if n % i == 0:
            # If i does divide n, then return i
            return i

    # If no prime factors have been found, then n is a prime number
    return n

