

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
    if n <= 1:
        return n
    if n > 100000:
        return -1
    if n % 2 == 0:
        return 1
    i = 2
    while i < n:
        if i % 100000 == 0:
            return -1
        if n % i == 0:
            break
        i += 1
    if n % 100000 == 0:
        return -1
    i = 1
    while i < n:
        if n % i == 0:
            break
        i += 1
    prime_fib(i)
    prime_fib(n-i)
    return n
