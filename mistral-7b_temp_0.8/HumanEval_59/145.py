

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # 1. n >= 2 and not prime
    # 2. n must be factorable
    # 3. n not equal to 1
    # 4. n not equal to 0
    # 5. n not equal to None

    if n <= 1:
        return None
    else:
        i = 2
        while i < n:
            if n % i == 0:
                n = n / i
                return i
            else:
                i += 1

