

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
    a, b = 2, 3
    while True:
        fib = a + b
        if is_prime(fib):
            if n == 1:
                return a
            n -= 1
            a, b = b, fib
        else:
            a += 2
            b += 2

