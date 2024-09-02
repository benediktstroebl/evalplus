

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

    i = 2
    j = 3
    while n:
        i, j = j, j+i
        if j % 2 == 0:
            j += 1
        if not prime_fib(j):
            j += 2
        n -= 1
    return j

