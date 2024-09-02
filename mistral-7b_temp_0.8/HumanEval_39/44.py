

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

    if n <= 1:
        return 2

    fibs = [2, 3]
    nth = 3
    while nth < n:
        fibs.append(fibs[-1] + fibs[-2])
        nth += 1

    for fib in fibs:
        if all(fib % i != 0 for i in range(2, fib + 1)):
            return fib
    raise Exception(f"{n} does not have a prime Fibonacci number")

