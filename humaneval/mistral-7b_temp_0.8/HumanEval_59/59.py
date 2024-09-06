

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # is_prime is a helper function which returns true if n is prime and false otherwise
    def is_prime(n: int):
        if n < 2:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True
    while True:
        if is_prime(n):
            return n
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                n = n // i
                break
        return n
