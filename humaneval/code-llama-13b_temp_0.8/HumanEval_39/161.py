

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
    a = 1
    b = 1
    c = 0
    n_of_fib = 0
    while True:
        c = a + b
        a = b
        b = c
        n_of_fib += 1
        if n_of_fib >= n:
            break
    return c
