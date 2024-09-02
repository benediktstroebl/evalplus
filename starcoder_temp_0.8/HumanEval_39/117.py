

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

    # a list of Fibonacci numbers
    fib = [1, 2]
    i = 2
    # a list of prime numbers
    primes = [2]

    while True:
        n_fib = fib[i - 1] + fib[i - 2]
        fib.append(n_fib)
        if is_prime(n_fib):
            primes.append(n_fib)
            if len(primes) == n:
                return n_fib
        i += 1
