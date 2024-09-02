

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
    # Use Fibonacci generator
    a, b = 0, 1
    while b < n:
        a, b = b, a + b

    # is_prime here is an oddity,
    #   we can use it to find all primes in [2, sqrt(n)]
    return a if is_prime(a) and is_prime(n-a) else None
