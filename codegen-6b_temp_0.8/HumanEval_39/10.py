

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
    if n <= 0:
        return -1

    if n == 1:
        return 1

    i = 1
    ind = 1
    ind2 = 0
    while n > ind:
        ind = i + ind2
        i, ind2 = ind, i
    return ind

