

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
    nth_prime = 0
    a = 1
    b = 1
    while nth_prime < n:
        a, b = b, a + b
        if is_prime(b):
            nth_prime += 1
    return b

