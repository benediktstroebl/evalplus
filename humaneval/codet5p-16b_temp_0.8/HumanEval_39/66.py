

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

    prev = 0
    cur = 1
    i = 1
    while i < n:
        prev, cur = cur, prev + cur
        i += 1
        if not is_prime(cur):
            cur += 1
    return cur
