

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

    if n <= 0:
        raise ValueError("n should be greater than 0.")

    if n == 1:
        return 2

    i = 1
    fib_n = 1
    fib_n2 = 0
    while True:
        i += 1
        fib_n, fib_n2 = fib_n + fib_n2, fib_n
        if is_prime(fib_n) and is_prime(fib_n2):
            if i == n:
                return fib_n
