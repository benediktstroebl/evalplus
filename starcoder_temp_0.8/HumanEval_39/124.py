

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
    if n == 1:
        return 2
    fibs = fib_generator()
    primes = prime_generator()
    for i in range(1, n):
        f = next(fibs)
        p = next(primes)
        while not is_prime(f):
            f = next(fibs)
            p = next(primes)
    return f
