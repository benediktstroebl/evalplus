

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
    if n <= 2:
        return n
    else:
        f0, f1 = 2, 3
        i = 2
        while i < n:
            f2 = f0 + f1
            f0 = f1
            f1 = f2
            i += 1
        return f2

