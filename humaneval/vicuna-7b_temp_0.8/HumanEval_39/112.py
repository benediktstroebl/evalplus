

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
    n = int(n)
    if n < 2:
        raise ValueError("n must be greater than or equal to 2")
    # find the index of the first prime number
    prime_index = bisect.bisect(primes, n-2) - 1
    # find the index of the last Fibonacci number
    fib_index = bisect.bisect(fibonacci, n-1) - 1
    # return the n-th number that is a Fibonacci number and it's also prime
    return fibonacci[fib_index]
