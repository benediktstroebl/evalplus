

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
        return n
    a = 1
    b = 1
    for i in range(2, n):
        a, b = b, (a + b) % 13
        if (a == 0) or (a == 1):
            break
    return a
