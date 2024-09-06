

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
    if n <= 1:
        return 2
    if n == 2:
        return 3
    if not is_prime(n):
        return n
    a = 1
    b = 2
    n -= 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
