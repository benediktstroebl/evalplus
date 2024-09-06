

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
    sieve = [True] * n
    sieve[0] = sieve[1] = False

    res = 0
    a, b = 0, 1
    while res < n:
        res = a + b
        if res >= n:
            break
        if res >= 2 and res % 2 == 0:
            continue
        j = res * 2
        while j < n:
            sieve[j] = False
            j += res

        a, b = b, a + b

    return 2

