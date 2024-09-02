

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

    a, b = 0, 1
    while a < n:
        a, b = b, a+b
        if b%2 == 0:
            b = b+1
        elif a > n:
            return a-1
        if is_prime(b):
            b = b+1
        else:
            b = b+2
    return b-1
