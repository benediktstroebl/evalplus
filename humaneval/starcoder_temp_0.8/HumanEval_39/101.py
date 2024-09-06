

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
    counter, fib, p, f = 1, 2, 0, 0
    while counter <= n:
        f = fib + 1
        fib = f if isprime(fib) else fib
        counter += 1
    return fib
