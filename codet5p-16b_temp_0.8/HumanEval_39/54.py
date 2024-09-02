

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

    prev, cur = 1, 1
    i = 2
    while i < n:
        prev, cur = cur, prev + cur
        i += 1
        if cur % prev == 0 and is_prime(cur):
            n = i
    return cur

