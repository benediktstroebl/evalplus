

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
    n_1, n_2 = 0, 1
    i = 3
    while n_1 < n:
        if is_prime(i) and is_fibonacci(i):
            n_1, n_2 = n_1 + n_2, n_1
        i += 2
    if n_1 == n:
        return i

