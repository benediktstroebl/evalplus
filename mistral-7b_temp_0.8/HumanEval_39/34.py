

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
    fibs = [1, 1]
    while len(fibs) < n:
        if all(fibs[-1] % prime for prime in fibs[:-1]):
            fibs.append(fibs[-1] + fibs[-2])
        else:
            fibs.append(fibs[-1] - fibs[-2])
    return fibs[-1]

