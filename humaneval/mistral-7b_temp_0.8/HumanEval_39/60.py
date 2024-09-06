

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
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    f1 = 1
    f2 = 1
    f3 = 2
    count = 3
    while count < n:
        f4 = f1 + f2
        f1, f2 = f2, f4
        count += 1
        if f4 % 2 != 0:
            f3 = f4
    return f3

