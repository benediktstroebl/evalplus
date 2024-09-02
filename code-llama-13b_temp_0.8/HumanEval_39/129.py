

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
    if not isinstance(n, int):
        raise ValueError("n must be positive integer")

    # Fibonacci sequence
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if is_prime(b):
            if n == 1:
                return b
            else:
                n -= 1

