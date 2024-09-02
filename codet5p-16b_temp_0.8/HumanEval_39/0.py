

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

    p1, p2 = 0, 1
    for i in range(n):
        p1, p2 = p2, p1 + p2
        if is_prime(p2):
            return p2
    return -1

