

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
    from math import floor, sqrt
    def is_prime(x: int) -> bool:
        """
        is_prime determines if a number is prime.
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(5)
        True
        >>> is_prime(6)
        False
        >>> is_prime(7)
        True
        >>> is_prime(8)
        False
        >>> is_prime(9)
        False
        >>> is_prime(10)
        False
        """
        if x == 2 or x == 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        for i in range(5, int(sqrt(x)) + 1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False
        return True

    def fib(n: int) -> int:
        """
        fib returns n-th number that is
