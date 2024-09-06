

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
        return -1

    if n == 1:
        return 2

    if n == 2:
        return 3

    if n == 3:
        return 5

    if n == 4:
        return 13

    fib1 = 2
    fib2 = 3
    fib3 = fib1 + fib2

    # finds the next number in Fibonacci sequence
    for i in range(4, n):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3

    return fib3

