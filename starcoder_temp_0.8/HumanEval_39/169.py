

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
    primes = prime_list(10000)
    i = 2
    fibo = 2
    while i < n:
        fibo = fibo + primes[i-1]
        i = i + 1
    return fibo
