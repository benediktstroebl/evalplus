

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

    assert 0 < n, "Argument to prime_fib() must be positive"
    fib, last = 1, 1
    while True:
        if fib % 2 == 0:
            fib, last = last, fib + last
        else:
            for i in range(3, int(fib**0.5) + 1, 2):
                if fib % i == 0:
                    fib, last = last, fib + last
                    break
            else:
                return fib
        if n == fib:
            return fib
        n -= 1

