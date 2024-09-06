

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

    p1 = 1
    p2 = 2
    fib = 0
    for i in range(1, n):
        fib = p1 + p2
        p1 = p2
        p2 = fib
        if is_prime(fib):
            print(fib)
        else:
            continue

