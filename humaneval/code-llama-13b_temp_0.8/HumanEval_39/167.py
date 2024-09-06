

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
    # counting Fibonacci numbers
    fib_1, fib_2 = 1, 1
    for i in range(n - 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    # looping for prime numbers
    primes = []
    while len(primes) < n:
        if is_prime(fib_1):
            primes.append(fib_1)
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    return primes[-1]

