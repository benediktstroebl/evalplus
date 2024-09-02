

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(num: int) -> bool:
        for i in range(2, int(num**(0.5)) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(2, int(n**(0.5)) + 1):
        if n % i == 0:
            if is_prime(i):
                return i

    return n

