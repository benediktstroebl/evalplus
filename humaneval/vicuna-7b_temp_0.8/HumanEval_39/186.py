

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
    # Check if n is a prime number
    if n % 2 != 0:
        return 1
    if n % 3 == 0:
        return 2
    i = 1
    limit = 49
    while i <= limit:
        if (i % (i - 1) == 0 and i % (i + 1) == 0):
            return 1
        i += 1
    return 1
