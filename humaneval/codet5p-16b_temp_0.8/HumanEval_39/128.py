

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

    p1, p2 = 2, 3
    cnt = 0
    while cnt!= n - 1:
        p1, p2 = p2, p1 + p2
        cnt += 1
        if p2 % p1 == 0:
            p2 = p2 // p1
        if p1 == p2:
            p1 = 2
            p2 = 3
    return p2

