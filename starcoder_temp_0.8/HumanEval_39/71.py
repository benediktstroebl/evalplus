

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
    if n == 1:
        return 2
    if n == 2:
        return 3
    f1 = 2
    f2 = 3
    count = 3
    while count < n:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        if isprime(f3):
            count += 1
    return f3
