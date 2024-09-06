

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
    if n <= 2:
        return 2, 3
    x, y = 2, 3
    for i in range(3, n+1):
        x, y = y, x + y
        if y > n:
            break
        if is_prime(y):
            return y
