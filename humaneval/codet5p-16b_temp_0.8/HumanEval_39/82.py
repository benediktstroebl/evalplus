

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

    p = 2
    q = 3
    count = 3
    while count <= n:
        p, q = q, q + p
        if (pow(p, 2)) + (pow(q, 2)) == pow(q + p, 2):
            count += 1
    return q + p

