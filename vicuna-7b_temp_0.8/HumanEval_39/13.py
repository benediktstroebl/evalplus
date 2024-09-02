

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
    if n < 2:
        return 2
    if n == 2:
        return 3

    if n in [2, 3]:
        return n + 1

    f1, f2 = 0, 1
    while f1 < n:
        f1, f2 = f2, f1 + f2

    p = 1000000
    while p <= n // 2 and (p - 2 * n % p) % p != 0:
        p += 1

    i = 0
    while True:
        p1 = 1000000 * i + p // 2
        if p1 > n and (p1 - 2 * n % p1) % p1 != 0:
            break
        i += 1
    j = 0
    while True:
        p1 = 1000000 * j + p // 2
        if p1 > n and (p1 - 2 * n % p1) % p1 != 0:
            break
        j += 1

    return f1 * f2 * p1 * p2

prime_fib = prime_fib(1000)
