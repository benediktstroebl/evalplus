

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

    primes = []
    i = 1
    while len(primes)!= n:
        if is_prime(i):
            if is_fib(i):
                primes.append(i)
        i += 1
    return primes[n - 1]
