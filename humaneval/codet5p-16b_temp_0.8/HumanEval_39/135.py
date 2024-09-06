

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

    f1, f2 = 1, 1
    c = 0
    while True:
        f1, f2 = f1+f2, f1
        c += 1
        if c == n:
            break
    p = 0
    while True:
        p = f1 % c
        if p == 0 and c > 1:
            break
        f1 += 1
    return f1

