

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
    a = 0
    b = 1
    if n <= 0:
        return
    if n == 1:
        return a
    if n == 2:
        return b

    count = 2

    while True:
        b, a = b + a, b
        if is_prime(b):
            count += 1
            if count == n:
                return b

