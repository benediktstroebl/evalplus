

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
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be positive integer")
    fib_1, fib_2 = 1, 1
    count = 2
    while True:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        count += 1
        if is_prime(fib_1) and is_prime(fib_2):
            if count == n:
                return fib_1
            elif count == n + 1:
                return fib_2

