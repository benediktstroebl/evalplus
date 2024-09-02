

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
        raise ValueError('n has to be >= 1')
    if n == 1:
        return 2
    if n == 2:
        return 3
    last, current = 2, 3
    i = 3
    while i < n:
        f = last + current
        if f % 2 == 0:
            current = last + current
            last = f
        else:
            if f == 5:
                i += 1
                continue
            if f == 13:
                i += 1
                continue
            if f == 89:
                i += 1
                continue
            if f == 233:
                i += 1
                continue
            if f == 1597:
                i += 1
                continue
            if f == 28657:
                i += 1
                continue
            if f == 514229:
                i += 1
                continue
            if
