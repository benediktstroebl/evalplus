

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
        return n
    elif n == 3:
        return 5

    f1 = 1
    f2 = 2
    for i in range(3, n+1):
        f = f1 + f2
        f1 = f2
        f2 = f
        if is_prime(f):
            if is_fib(f):
                return f

