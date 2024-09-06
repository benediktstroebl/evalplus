

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
    fib_n_minus_2, fib_n_minus_1 = 2, 3
    while True:
        fib_n = fib_n_minus_1 + fib_n_minus_2
        if fib_n >= n:
            return fib_n
        if is_prime(fib_n):
            fib_n_minus_2 = fib_n_minus_1
            fib_n_minus_1 = fib_n
