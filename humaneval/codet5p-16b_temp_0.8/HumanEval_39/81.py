

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

    fib = 1
    fib_prev = 1
    while True:
        fib = fib_prev + fib
        fib_prev = fib
        if is_prime(fib):
            if n == 1:
                return fib
            n -= 1
        else:
            fib = fib_prev - fib

