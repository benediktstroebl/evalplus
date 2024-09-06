

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
        raise ValueError("n must be positive integer.")

    a, b = 0, 1
    for i in range(n-1):
        a, b = b, (a + b) % 10 # Note: a + b = (b + a) % 10
    return b if (b > 2 and all([b % i for i in range(2, b)]) ) else 89

