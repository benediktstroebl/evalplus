

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
    # p1 and p2 are primes that are Fibonacci numbers.
    p1 = 2
    p2 = 3
    f = 3
    while True:
        f = p1 + p2
        if is_prime(f) == True:
            p1 = p2
            p2 = f
            if n == 1:
                return f
            n -= 1

