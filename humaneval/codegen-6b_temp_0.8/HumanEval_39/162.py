

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
    if n == 2:
        return 3
    fib1 = 1
    fib2 = 2
    fibn = 3
    while n > 2:
        fibn = fib1 + fib2
        fib1 = fib2
        fib2 = fibn
        n -= 1
    if is_prime(fibn):
        return fibn

