

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

    if n == 1:
        return 2
    elif n == 2:
        return 3

    n_fib = 3
    a = 2
    b = 3
    for i in range(n - 3):
        n_fib = a + b
        a, b = b, n_fib

    while not is_prime(n_fib):
        n_fib += 2

    return n_fib

