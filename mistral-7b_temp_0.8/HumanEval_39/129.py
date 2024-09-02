

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
    a, b = 0, 1
    while a <= n:
        if is_prime(a):
            if a == n:
                return a
        a, b = b, a + b
    raise ValueError("No Fibonacci prime number for %d" % n)

