

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

    fib = [1, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])

    for i, j in enumerate(fib):
        if j > 1 and j % 2 != 0:
            return j
    return fib[-1]

