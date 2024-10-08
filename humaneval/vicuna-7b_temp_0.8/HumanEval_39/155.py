

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
        return n
    if n % 2 == 0:
        return 1
    if n % 3 == 0:
        return 2
    while True:
        candidate = (1000000 + prime_fib(n // 2) + prime_fib(n // 3)) // n
        if candidate % n == 0:
            return candidate
        if candidate > 1000000:
            return candidate
        if candidate < 2:
            return candidate
