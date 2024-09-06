

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
    # check if n is prime
    if n < 2:
        return 1
    if n == 2:
        return 2
    if n % 2 == 0:
        return 1
    # check if n is Fibonacci
    if n > 2:
        a, b = 1, 1
        while a < n:
            a, b = b, a + b
        return b
    # if n is not Fibonacci, return 1
    return 1
