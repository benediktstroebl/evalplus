

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

    n = n - 1
    count = 0
    fib = 1
    while count < n:
        fib = fib + 2
        if is_prime(fib):
            count += 1
    return fib


