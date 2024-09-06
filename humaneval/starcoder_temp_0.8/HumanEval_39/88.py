

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
    i = 1
    while True:
        f = fib(i)
        if f > n:
            break
        i += 1
    p = prime(f)
    while True:
        f = fib(i)
        if p and f > n:
            break
        i += 1
        p = prime(f)
    return f

