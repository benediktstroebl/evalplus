

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
    if n <= 2:
        return n
    while n % 2 == 0:
        n = n / 2
        if n > 11:
            break
    fib = 0, 1
    for i in range(n, 1, -1):
        fib[1] = fib[0] + fib[1]
        if fib[1] > n:
            break
    for p in range(11, n - 1):
        if fib[0] < p:
            break
        if fib[0] % p == 0:
            return fib[0]
    return fib[0]

@task
