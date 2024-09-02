

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
    f0 = 0
    f1 = 1
    if n == 1:
        return f0
    if n == 2:
        return f1
    if n == 3:
        return f1
    while True:
        f0, f1 = f1, f1 + f0
        n -= 1
        if n == 1:
            return f0
        if n == 2:
            return f1
        if f0 < f1:
            n -= 1
        if f0 > f1:
            break
        if n == 1:
            return f1
        if n == 2:
            return f0
        if is_prime(f0):
            return f0
        if is_prime(f1):
            return f1

