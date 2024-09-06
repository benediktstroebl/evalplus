

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
    if is_fibonacci(n):
        return n
    i = 2
    while n > i:
        if is_prime(i):
            n -= i
        i += 1
    return i - 1
