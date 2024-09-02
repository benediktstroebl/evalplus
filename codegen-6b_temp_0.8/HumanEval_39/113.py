

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
        raise ValueError('n must be a positive integer')
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 2, 3
        i = 3
        while i <= n:
            a, b = b, (a + b)
            i += 1
        if is_prime(b):
            return b
        else:
            return None
