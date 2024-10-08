

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
    if n < 0 or n > 10:
        return -1
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n % 2 != 0:
        return -1
    if n in [3, 5, 8, 13]:
        return n
    is_prime, r = prime_fib_rec(n)
    if r is not None:
        return r
    return None
