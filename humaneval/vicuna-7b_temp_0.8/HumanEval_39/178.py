

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
    a, b = 0, 1
    result = 0
    for i in range(n):
        if a < b:
            if is_prime(a):
                result = a
            a = b
            b = (b + a) % 1000000
        else:
            if is_prime(b):
                result = b
            b = (b + a) % 1000000
    return result