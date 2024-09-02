

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
        return 2
    else:
        fib = 1
        a = 0
        b = 1
        p = 1
        for i in range(2, n):
            if i % 2 == 0:
                a += fib
            else:
                b += fib
                fib *= 2
                fib += b
                p *= 2
                p += a
                a = b
                b = fib
        return p
