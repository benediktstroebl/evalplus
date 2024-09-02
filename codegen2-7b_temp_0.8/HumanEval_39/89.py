

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
    i = 0
    j = 1
    nth = 2
    while nth < n:
        i, j = j, i + j
        if j % n == 0:
            break
        nth += 1
    return nth
