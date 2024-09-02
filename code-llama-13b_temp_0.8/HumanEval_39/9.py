

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
    f1 = 1
    f2 = 1
    f = 0
    p1 = 1
    p2 = 1
    p = 0
    k = 2
    while k < n:
        f = f1 + f2
        f1 = f2
        f2 = f
        if f > p2:
            p = p2
            p1 = p2
            p2 = f
        else:
            p = p1
            p1 = f
        if is_prime(p):
            k += 1
    return p

