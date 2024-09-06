

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
    if not isinstance(n, int):
        raise TypeError("n should be a positive integer")
    if n < 1:
        raise ValueError("n should be a positive integer")

    primes = [2, 3, 5, 7]
    f = [0, 1]

    while len(primes) < n:
        f.append(f[len(f) - 1] + f[len(f) - 2])
        if f[len(f) - 1] % 2 == 0:
            p = 2
        else:
            p = 3
        while True:
            if f[len(f) - 1] % p == 0:
                break
            p += 2
        if p == f[len(f) - 1]:
            primes.append(p)
    return primes[n - 1]

