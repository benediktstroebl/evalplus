

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
    a, b, count = 0, 1, 0
    while True:
        if not is_prime(b):
            a, b = b, a + b
            continue
        count += 1
        if count == n:
            return b
        a, b = b, a + b

