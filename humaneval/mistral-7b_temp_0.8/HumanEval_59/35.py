

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        raise ValueError("n must be greater than 1.")

    def is_prime(n: int):
        """Return True if n is prime and False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

    def largest_prime_factor(n: int):
        """Return the largest prime factor of n. Assume n > 1 and is not a prime.
        """
        if is_prime(n):
            return n

        for i in range(n // 2, 1, -1):
            if n % i == 0 and is_prime(i):
                return i

        return 1

