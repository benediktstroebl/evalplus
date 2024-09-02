

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
    if n < 1:
        raise ValueError("n must be greater than 0")
    fib_primes = [2]
    fib_prev = 1
    fib = 2

    while len(fib_primes) < n:
        # check if fib is prime
        if all(fib % i for i in range(2, int(fib**0.5) + 1)):
            fib_primes.append(fib)
        fib = fib_prev + fib
        fib_prev = fib - fib_prev
    return fib_primes[-1]

