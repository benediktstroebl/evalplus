

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
    count = 0
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
        if prime(fib2) and count == n:
            return fib2

