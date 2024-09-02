

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
    assert n >= 1
    # sieve of eratosthenes
    sieve = [True] * 1000
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = False

    for i in range(n):
        if sieve[i + 1]:
            return i + 1
    return -1
