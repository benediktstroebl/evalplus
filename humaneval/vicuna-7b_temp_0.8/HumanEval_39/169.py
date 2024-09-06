

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
    f_n, f_n_prime = fib(n)
    while f_n_prime % 2 != 0:
        f_n_prime, f_n_prime_prime = fib(n_prime)
        f_n_prime, f_n_prime_prime = f_n_prime_prime + f_n_prime, f_n_prime - f_n_prime_prime
    return f_n_prime
