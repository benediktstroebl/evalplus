

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
    i, j = 1, 1
    while True:
        if is_prime(i) and is_fib(i):
            n -= 1
        if n == 0:
            return i
        i, j = j, i + j

