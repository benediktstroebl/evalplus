

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
    if n < 2:
        return 1
    elif n < 11:
        return prime_fib(n-2) + prime_fib(n-3)
    elif n % 2 != 0:
        return 0
    else:
        f = [2, 3]
        while f[0] < n:
            f.append(f[0] + f[1])
        return f[0]
