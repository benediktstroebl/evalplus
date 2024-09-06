

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
    assert n > 0
    if n == 1:
        return 2
    fib = [2]
    cur = fib[0]
    while True:
        if cur % 2 == 0:
            cur += 1
        else:
            cur += 2
        fib.append(cur)
        if isPrime(cur):
            if fib.index(cur) + 1 == n:
                return cur

