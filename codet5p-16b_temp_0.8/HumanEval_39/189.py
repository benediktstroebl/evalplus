

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

    fib = lambda n: (n <= 1 and 1) or (fib(n - 1) + fib(n - 2))
    prime = lambda n: n == 2 or all(n % i for i in range(2, n))
    fibs = [i for i in range(n) if prime(fib(i))]
    return next(fib for fib in fibs if fib > 1 and fib + fib < n)

