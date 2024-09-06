

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
    # your code here
    fib_n = fib(n)
    primes = primes_sieve(n)
    prime_fib_n = primes[fib_n]
    return prime_fib_n
