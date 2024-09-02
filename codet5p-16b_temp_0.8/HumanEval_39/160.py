

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """

    from functools import lru_cache
    from itertools import count

    fib_n = lambda n: int((1 + 5 ** 0.5) / 2 ** n / 5 ** 0.5)
    fib_sequence = count(1, 2)
    fib_count = count(1, 2)

    def is_prime(n: int):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    @lru_cache
    def fib_prime(n: int):
        if n == 1:
            return 2
        if n == 2:
            return 3
        a, b = next(fib_sequence), next(fib_sequence)
        for _ in range(3, n):
            c = a + b
            if is_prime(c):
                a, b = b, c
            else:
                return c
        return b

    return fib_prime(n)

