

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
    n_th_fib = fibonacci(n - 1)
    while not is_prime(n_th_fib):
        n_th_fib = fibonacci(n)
    return n_th_fib

