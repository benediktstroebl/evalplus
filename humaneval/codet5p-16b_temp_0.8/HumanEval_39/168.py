

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

    i = 1
    while True:
        f = (i ** 2 + i + 1) / 2
        if is_prime(f):
            break
        i += 1

    i += 1
    while True:
        f = (i ** 2 + i + 1) / 2
        if is_prime(f) and is_fibonacci(f):
            break
        i += 1

    return f

