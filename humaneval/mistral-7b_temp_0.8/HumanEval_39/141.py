

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
    if n < 3:
        return 2

    p1, p2, fib, next_prime = 2, 3, 0, 5
    while fib < n:
        if all((next_prime % p1, next_prime % p2)):
            fib += 1
            p1, p2 = p2, fib
            next_prime += 1
    return next_prime

