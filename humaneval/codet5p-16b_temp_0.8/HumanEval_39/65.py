

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

    fib1 = 1
    fib2 = 1
    k = 0
    while k < n:
        fib3 = fib1 + fib2
        fib1, fib2 = fib2, fib3
        k += 1
        if (fib3 % 2) == 0:
            fib3 = fib3 + 2
            if (fib3 % 3) == 0 and (fib3 % 5) == 0 and (fib3 % 7) == 0 and (fib3 % 11) == 0:
                k = n
    return fib3

