

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
    n_1 = n - 1
    n_2 = n - 2
    if n % 2 == 0:
        return n - 1
    if n % 3 == 0:
        return n - 1
    if n % 5 == 0:
        return n - 1
    if n % 8 == 0:
        return n - 1
    if n % 13 == 0:
        return n - 1
    if n % 21 == 0:
        return n - 1
    if n % 34 == 0:
        return n - 1
    if n % 55 == 0:
        return n - 1
    if n % 89 == 0:
        return n - 1
    if n % 143 == 0:
        return n - 1
    if n % 233 == 0:
        return n - 1
    if n % 377 == 0:
        return n - 1
    if n % 610 == 0:
        return n - 1
    if n % 1215 == 0:
        return n - 1
    if n % 2431 == 0:
        return n - 1
    if n % 4863 == 0:
        return n - 1
    if n % 9729 == 0:
        return n - 1
    if n % 19457 == 0:
        return n - 1
    if n % 38895 == 0:
        return n - 1
    if n % 77791 == 0:
        return n - 1
    if n % 155583 == 0:
        return n - 1
    if n % 292173 == 0:
        return n - 1
    if n % 583519 == 0:
        return n - 1
    if n % 1166979 == 0:
        return n - 1
    if
