

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
    def is_prime(n: int):
        """
        is_prime returns whether n is prime number or not.
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
        if n <= 1:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

    def fib(n: int):
        """
        fib returns n-th number of Fibonacci series.
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
        if n <= 1:
            return 1
        elif n == 2:
            return 1
        else:
            return fib(n - 2) + fib(n - 1)

    for i in range(2, n):
        if is_prime(fib(i)):
            return fib(i)
