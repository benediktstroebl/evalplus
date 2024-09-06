

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # use the Sieve of Eratosthenes algorithm to find prime numbers less than n
    # and then check if the square of any of them is greater than n
    # if not, it must be the largest prime factor
    modulo = 2
    for i in range(3, n + 1, 2):
        is_prime = True
        for j in range(2, i + 1):
            if (modulo ** 2) % j == 0:
                is_prime = False
                break
        if is_prime:
            # if the square of this number is greater than n, then it's not prime
            if (modulo ** 2) >= n:
                return modulo
    # if we get here, we know that the largest prime factor is less than n
    # and is not prime
    return n
