

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
    if n <= 1:
        return n
    a = 1
    b = 1
    fib = 2
    while True:
        fib = a + b
        if is_prime(fib):
            a = b
            b = fib
            if fib==n:
                return fib
