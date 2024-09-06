

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
    primes = []
    while len(primes) < n:
        i += 1
        if isprime(i):
            primes.append(i)
    i = 2
    while len(primes) < n:
        i += 1
        if is_fib_prime(i):
            primes.append(i)
    return primes[n-1]
