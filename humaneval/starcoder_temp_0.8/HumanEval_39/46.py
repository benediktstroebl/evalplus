

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
    n_th = [1, 1]
    for _ in range(n - 1):
        n_th = [n_th[1], n_th[0] + n_th[1]]
    return next_prime(n_th[0])

