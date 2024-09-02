

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
        Check if number n is a prime number.
        >>> is_prime(0)
        False
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
        >>> is_prime(6)
        False
        >>> is_prime(7)
        True
        >>> is_prime(11)
        True
        >>> is_prime(12)
        False
        >>> is_prime(13)
        True
        >>> is_prime(14)
        False
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    i = 0
    fib = 0
    fib_1 = 1
    while i < n:
        fib_2 = fib + fib_1
        fib = fib_1
        fib_1 = fib_2
        i += 1
    if is_prime(fib):
        return fib
    return prime_fib(n - 1)
