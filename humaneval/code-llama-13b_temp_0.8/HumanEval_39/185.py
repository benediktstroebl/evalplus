

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
    primes = [True] * (n + 1)
    for i in range(2, int(n ** 0.5 + 1)):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    prime_fibs = [2]
    i = 1
    while i < n:
        a, b = prime_fibs[-2], prime_fibs[-1]
        c = a + b
        if c > n:
            break
        if primes[c]:
            prime_fibs.append(c)
            i += 1
    return prime_fibs[n-1]

