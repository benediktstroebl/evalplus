

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
    f0 = 1
    f1 = 2
    for i in range(3, n+1):
        f0, f1 = f1, f0 + f1
        while not is_prime(f0):
            f0, f1 = f1, f0 + f1
    return f0
