

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
    if n < 1:
        raise ValueError
    n -= 2
    if n < 0:
        raise ValueError
    fibs = [1, 1]
    for i in range(n):
        fibs.append(fibs[-1] + fibs[-2])
    for f in fibs[n:]:
        if f > 1 and all(f % x != 0 for x in range(2, f)):
            return f
    raise ValueError

