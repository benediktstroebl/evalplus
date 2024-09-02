

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
    f = [0, 1]
    j, i = 0, 1
    while j < n:
        if j > i:
            j = (i + j) % (2 * n)
        f[i] = f[j]
        i, j = j, i + f[j]
    return f[n-1]
