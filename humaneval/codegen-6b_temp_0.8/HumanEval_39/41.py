

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
    f_1 = 1
    f_2 = 1
    f_3 = 5
    while f_3 <= n:
        f_2, f_3 = f_3, f_2 + f_3
    return f_2
