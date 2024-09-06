

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

    fib_1, fib_2, index = 1, 2, 1
    while index!= n:
        fib_1, fib_2 = fib_2, fib_2 + fib_1
        index += 1
        if prime_fib(index):
            continue
        else:
            return fib_2

