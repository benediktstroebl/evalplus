

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

    n = n + 2  # There are no primes below 2
    a = [0] * n
    a[0] = 1
    i = 1
    while i < n:
        a[i] = a[i - 2] + a[i - 1]
        if a[i] >= n:
            a[i] %= n
        if a[i] == 1 and i > 2:
            i = n
        else:
            i += 1
    return a[n - 2]

