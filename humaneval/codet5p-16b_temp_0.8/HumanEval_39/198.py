

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

    f1 = 0
    f2 = 1
    index = 1
    while True:
        f3 = f1 + f2
        if f3 > n:
            break
        if f3 % 2 == 0 or f3 % 3 == 0 or f3 % 5 == 0:
            f1 = f2
            f2 = f3
            index += 1
            continue
        f1 = f2
        f2 = f3
        index += 1
    return f3
