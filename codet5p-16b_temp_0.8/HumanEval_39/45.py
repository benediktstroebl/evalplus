

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

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    fibs = [2, 3, 5, 8, 13, 21, 34, 55]
    for i in range(len(primes), n + 1):
        if i < len(fibs):
            if i == 7:
                fibs.append(fibs[-1] + fibs[-2])
            else:
                fibs.append(fibs[-2] + fibs[-1])
        else:
            fibs.append(fibs[-1] + fibs[-2])
            fibs = [2, 3, 5, 8, 13, 21, 34, 55]
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        while fibs[-1] % primes[-1]!= 0:
            del primes[-1]
        if
