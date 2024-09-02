

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
    assert n > 0
    a, b, c = 1, 1, 1
    while True:
        c = a + b
        a, b = b, c
        if c <= n:
            continue
        elif n == c:
            return n
        else:
            break

