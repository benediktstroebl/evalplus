

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

    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return b if [i for i in range(2, b) if b % i] else b + 1

