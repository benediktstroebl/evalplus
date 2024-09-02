

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
    if n < 2:
        raise ValueError(f"{n} is not a valid number")
    while True:
        x, y = 0, 1
        for i in range(n):
            x, y = y, x + y
            if is_prime(x):
                return x

