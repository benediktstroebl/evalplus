

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
    n_minus_1_prime = xbm.next_prime(n - 1)
    n_prime = xbm.next_prime(n)
    a = xbm.modular_exponentiation(n_minus_1_prime, n_prime, n_minus_1_prime)
    return a

