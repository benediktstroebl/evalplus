

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
    fib = [1, 1]
    while len(primes) < n:
        if is_fibonacci(fib[-1] + fib[-2]):
            primes.append(fib[-1] + fib[-2])
        fib.append(fib[-1] + fib[-2])
    return primes[-1]

