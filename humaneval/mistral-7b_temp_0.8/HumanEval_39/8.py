

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
    for i in range(1, n):
        if i == 1:
            fib = 1
        elif i == 2:
            fib = 1
        else:
            fib = fib_nth(i)
        if fib % 2 == 0 or fib == 1:
            continue
        for p in range(2, fib):
            if fib % p == 0:
                break
        else:
            return fib
