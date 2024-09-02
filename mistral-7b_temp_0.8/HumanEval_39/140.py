

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

    # We can use sieve of Eratosthenes to find all prime numbers up to n
    # and then use two pointers to find the n-th fibonacci number that is
    # prime.

    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False

    # Find the n-th fibonacci number that is prime
    i = 1
    j = 0
    while True:
        if primes[i + j]:
            if i + j == n:
                return i + j
        i, j = j, i + j

