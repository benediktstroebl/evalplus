

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
    if n < 2:
        return 2
    else:
        n = n - 1
        if n < 2:
            return 1
        if (n - 2) % 2 == 0:
            return 1
        else:
            a, b = 0, 1
            while (a < n // 2):
                b, a = a + b, a + b
            if a % 2 == 0:
                return 1
            else:
                return b
