

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

    n1 = 2
    n2 = 3
    f = 5
    k = 7
    while k <= n:
        if f % k == 0:
            n1, n2 = n2, f
            f = n1 + n2
            k = 7
        else:
            f = n1 + n2
            k = k + 2

    return f

