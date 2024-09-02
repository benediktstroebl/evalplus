

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

    fib1, fib2 = 1, 1
    for i in range(n - 1):
        fib1, fib2 = fib2, fib1 + fib2
        if is_prime(fib1):
            return fib1
    return None

