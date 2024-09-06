

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
    fib_n_1 = 1
    fib_n_2 = 2
    fib_n = 0
    prime = 0
    while n > 0:
        if prime_fib_number(fib_n_2):
            prime = fib_n_2
            n -= 1
            fib_n_1 = fib_n_2
            fib_n_2 = fib_n
        else:
            fib_n_2 = fib_n_1 + fib_n_2
    return prime
