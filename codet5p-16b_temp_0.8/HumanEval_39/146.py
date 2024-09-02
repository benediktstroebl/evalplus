

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

    fib_1, fib_2, prime = 0, 1, 1
    while prime_fib.counter!= n:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        prime = (fib_2 % fib_2 == 0)
        prime_fib.counter += 1
    return fib_2


