

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

    lst = [2]
    f = [2, 1]
    for i in range(n):
        f.append(f[i] + f[i + 1])
        if f[-1] % f[-2] == 0:
            continue
        if f[-1] % f[-3] == 0:
            continue
        if f[-1] % f[-4] == 0:
            continue
        lst.append(f[-1])
    return lst[-1]

