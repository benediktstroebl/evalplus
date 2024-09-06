

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
        return 1
    if n < 11:
        return 2
    if n % 2 == 0 or n % 3 == 0:
        return 2
    if not n % 2:
        return 3
    if n % 2 == 1:
        return 5
    if n % 3 == 0:
        return 13
    if not n % 3:
        return 89
    if n > 89:
        return 2
