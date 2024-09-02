

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
    i = 3
    f1 = 3
    f2 = 5
    while i < n:
        f = f1 + f2
        if f % 2!= 0 and f % 3!= 0 and is_prime(f):
            i += 1
            if i == n:
                return f
        f1, f2 = f2, f
