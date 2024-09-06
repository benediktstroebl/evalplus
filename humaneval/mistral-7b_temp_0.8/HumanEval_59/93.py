

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def factorize(n):
        while n % 2 == 0:
            yield 2
            n = n // 2
        while n % 3 == 0:
            yield 3
            n = n // 3
        i = 5
        while i * i <= n:
            if n % i == 0:
                yield i
                n = n // i
            else:
                i += 2
        if n > 1:
            yield n

    for f in factorize(n):
        if is_prime(f):
            return f

