

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
    fibonacci = {0: 0, 1: 1}
    def fib(n):
        if n not in fibonacci:
            fibonacci[n] = fib(n-1) + fib(n-2)
        return fibonacci[n]

    for i in range(2, n):
        nb = fib(i)
        if nb == 1:
            return 1
        for j in range(2, nb+1):
            if nb % j == 0:
                return fib(i)
        return fib(i)
