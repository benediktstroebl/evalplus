

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
    if n < 1:
        raise ValueError("n should be >= 1")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        f1 = prime_fib(n - 1)
        f2 = prime_fib(n - 2)
        # Fibonacci number
        f = f1 + f2
        # check if it's prime
        while not is_prime(f):
            f1, f2 = f2, f
            f = f1 + f2
        return f

