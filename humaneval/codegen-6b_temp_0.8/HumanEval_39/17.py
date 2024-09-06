

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
    if n == 1:
        return 2

    if n == 2:
        return 3

    prev, curr = 1, 1

    for _ in range(n - 1):
        prev, curr = curr, (prev + curr)

    i = 2
    while i * i <= curr:
        if curr % i == 0:
            return False
        i = i + 1

    return True

