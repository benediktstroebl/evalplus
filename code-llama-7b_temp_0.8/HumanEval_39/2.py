

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
    def _is_prime(n: int):
        """
        _is_prime returns True if n is a prime number, False otherwise
        >>> _is_prime(1)
        False
        >>> _is_prime(2)
        True
        >>> _is_prime(3)
        True
        >>> _is_prime(20)
        False
        """
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def _get_fibonacci_of(n: int):
        """
        _get_fibonacci_of returns n-th number of Fibonacci sequence
        >>> _get_fibonacci_of(1)
        1
        >>> _get_fibonacci_of(2)
        1
        >>> _get_fibonacci_of(3)
        2
        >>> _get_fibonacci_of(4)
        3
        """
        a = 1
        b = 1
        for _ in range(1, n):
            a, b = b, a+b
        return b

    def _get_pif(n: int):
        """
        _get_pif returns n-th number of primes in Fibonacci sequence
        >>> _get_pif(1)
        2
        >>> _get_pif(2)
        3
        >>> _get_pif(3)
        5
        >>> _get_pif(4)
        13
        """
        a, b = 1, 1
        count = 1
        while _is_prime(_get_fibonacci_of(count)):
            count += 1
        return count

    return _get_fibonacci_of(_get_pif(n))

