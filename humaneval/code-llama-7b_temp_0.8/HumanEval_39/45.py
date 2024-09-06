

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
    if n == 1:
        return 2
    if n == 2:
        return 3
    i = 2
    fib_prev = 2
    fib_curr = 3
    while i < n:
        fib_prev, fib_curr = fib_curr, fib_curr + fib_prev
        if is_prime(fib_curr):
            i += 1
    return fib_curr

