

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
    if n < 0 or n > 100:
        raise ValueError("Invalid input")
    if n == 1:
        return 2
    if n == 2:
        return 3
    fib = 0
    for i in range(2, n):
        fib = fib + (i * (i - 1))
    if prime(fib) and prime(fib - 1):
        return fib
    else:
        return None
