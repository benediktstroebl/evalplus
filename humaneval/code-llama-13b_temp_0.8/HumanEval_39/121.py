

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
    def fib(n):
        if n == 0 or n == 1:
            return n
        return fib(n-1) + fib(n-2)

    def prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    pfib = 1
    i = 0
    while i <= n:
        pfib = fib(i)
        if prime(pfib):
            i += 1
        else:
            i += 1
    return pfib

