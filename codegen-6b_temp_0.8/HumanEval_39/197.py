

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
    i = 1
    a = 1
    b = 1
    primes = [2, 3]
    while len(primes) < n:
        c = a + b
        if c % 2 == 0:
            c += 1
        for p in primes:
            if c % p == 0:
                break
        else:
            primes.append(c)
            i += 1
        a = b
        b = c
    return primes[-1]
