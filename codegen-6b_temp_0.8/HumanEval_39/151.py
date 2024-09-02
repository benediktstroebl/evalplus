

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
    p = 0
    fib1 = 1
    fib2 = 1
    while fib1 <= n:
        fib1, fib2 = fib2, fib1 + fib2
        if is_prime(fib2):
            p += 1
    return fib2
