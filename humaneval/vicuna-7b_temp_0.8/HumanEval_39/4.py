

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
    n_prime_fib = 1
    n_fib = 0
    n_prime = 1
    n_fib = 1

    while n_fib < n:
        if n_prime_fib % n_fib == 0:
            n_prime_fib = 1
        else:
            n_prime_fib = n_prime_fib + n_fib
            n_fib = n_fib + 1
            n_prime = n_prime * n_fib

    return n_prime_fib
