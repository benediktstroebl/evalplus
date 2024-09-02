

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
    slow = 1
    fast = 1
    fib = 1
    while fib < n:
        slow, fast = fast, slow + fast
        fib = fast + slow
    if fib == n:
        return fib
    else:
        return fib, fib % 10
