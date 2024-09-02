

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

    i, j = 0, 1
    p = [0] * n
    while True:
        i, j = j, i + j
        if j > n:
            break
        if p[j] == 0:
            p[j] = j
        else:
            continue
        for k in range(j * 2, n + 1, j):
            p[k] = 0
    return p[n]

