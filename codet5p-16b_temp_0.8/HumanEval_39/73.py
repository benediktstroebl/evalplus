

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
    fibs = [1, 1]
    i = 2
    while i < n:
        fibs.append(fibs[i - 1] + fibs[i - 2])
        i += 1
    for i in range(len(fibs)):
        if prime_fib(i):
            return fibs[i]
    return None

