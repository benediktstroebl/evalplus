

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

    lst = [0, 1, 1]
    while len(lst) <= n:
        lst.append(lst[-1] + lst[-2])
        if lst[-1] % 2 == 0:
            lst[-1] = 0
        if lst[-1] % 5 == 0:
            lst[-1] = 0
        if lst[-1] % lst[-2] == 0:
            lst[-1] = 0
    return lst[-1]
