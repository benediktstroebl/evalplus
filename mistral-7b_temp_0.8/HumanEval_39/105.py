

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
    a, b, f = 0, 1, 1
    while f < n:
        f = a + b
        a, b = b, f
        if f > 1 and not any(f % i == 0 for i in range(2, int(f**0.5) + 1)):
            return f

