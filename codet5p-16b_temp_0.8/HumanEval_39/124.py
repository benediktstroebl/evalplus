

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

    p, prev = 1, 1
    while p < n:
        prev, p = p, p + prev
    return prev if not any(prev % i == 0 for i in range(2, prev)) else None
