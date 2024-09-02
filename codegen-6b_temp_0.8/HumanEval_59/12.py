

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(n: int):
        if n % 2 == 0 and n > 2:
            return False
        return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))

    def factor(n: int):
        div = 3
        while not is_prime(n) and n % div:
            div += 2

        if is_prime(n):
            return n

        return factor(n // div)

    return factor(n)

