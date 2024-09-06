

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

    def is_prime(n: int) -> bool:
        """
        is_prime returns True if n is prime.
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(5)
        True
        """
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True

    def fib(n: int) -> int:
        """
        fib returns n-th number of Fibonacci sequence.
        >>> fib(0)
        0
        >>> fib(1)
        1
        >>> fib(2)
        1
        >>> fib(3)
        2
        >>> fib(4)
        3
        >>> fib(5)
        5
        """
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

    i = 1
    while True:
        if is_prime(fib(i)):
            n -= 1
        if n <= 0:
            return fib(i)
        i += 1

