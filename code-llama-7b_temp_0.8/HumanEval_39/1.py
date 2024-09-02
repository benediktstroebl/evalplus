

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
        raise ValueError("Input must be a positive integer.")
    n -= 1
    cnt = 0
    a, b = 2, 3
    while cnt < n:
        if is_prime(a):
            cnt += 1
        a, b = b, a+b
    return b

