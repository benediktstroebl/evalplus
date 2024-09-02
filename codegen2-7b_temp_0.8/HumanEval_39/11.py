

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
    if n == 1 or n == 2:
        return 2
    fib = 1
    prev = 2
    fib_len = 2
    for i in range(2, n):
        fib = fib + prev
        prev = fib_len
        fib_len = fib_len + prev
    return
