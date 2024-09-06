

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
    n_1 = 1
    n_2 = 1
    i = 2

    while i <= n:
        n_1 = prime_fib(n_1)
        n_2 = prime_fib(n_2)
        product = n_1 * n_2
        if product % i == 0:
            return i
        i += 1

    return n_1 * n_2
