

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
    if n < 0 or not n % 1 == 0:
        return None
    if n == 1:
        return 2
    if n == 2:
        return 3

    if not (is_prime(n - 1) and is_prime(n - 2)):
        return None

    while n > 4:
        if not is_prime(n - 1):
            return None
        n = n - 1
        if not is_prime(n - 2):
            return None
        n = n - 2

    return n
