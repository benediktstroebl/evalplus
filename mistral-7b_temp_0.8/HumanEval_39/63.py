

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
    fib_l = [2, 3]
    fib = 2
    i = 3
    while fib < n:
        fib = fib_l[0] + fib_l[1]
        fib_l.append(fib)
        fib_l = fib_l[1:]
        fib_l.append(fib)
        fib_l = fib_l[1:]
    return fib_l[-1] if fib_l[-1] < n else n

