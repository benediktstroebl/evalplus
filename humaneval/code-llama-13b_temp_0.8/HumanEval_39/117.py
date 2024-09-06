

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
    i = 2
    while True:
        n_1, n_2 = n_2, n_1 + n_2
        if is_prime(n_2) and check_fib(n_2):
            if i == n:
                return n_2
            i += 1

