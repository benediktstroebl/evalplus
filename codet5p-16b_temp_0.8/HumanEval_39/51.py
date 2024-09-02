

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

    p, f = 0, 1
    while p < n:
        if is_fibonacci(f) and is_prime(f):
            p += 1
        f += 1
    return f - 1

