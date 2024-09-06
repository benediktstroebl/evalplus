

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
    s = 0
    f0, f1 = 0, 1
    for _ in range(n):
        s = f0 + f1
        f0, f1 = f1, s
        if is_prime(s):
            return s

