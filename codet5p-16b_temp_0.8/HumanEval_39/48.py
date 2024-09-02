

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

    n_1, n_2 = 1, 1
    for i in range(n - 1):
        n_1, n_2 = n_2, n_1 + n_2
        if is_prime(n_2) and is_fib(n_2):
            return n_2

