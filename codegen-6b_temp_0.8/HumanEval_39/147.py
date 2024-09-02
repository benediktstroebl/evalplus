

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
    elif n == 2:
        return 3
    # find n-3, till n-3 = n-1
    # if n-3 is not prime it is a Fibonacci too
    # otherwise return it
    for i in range(1, n):
        if i == 1:
            fib_idex = 1
        else:
            fib_idex = i - 1
        if not is_prime(i):
            return i
    # if n-3 is prime
    # recursively find fib
    # n = n - 1
    # fib = fib + fib
    if n - 3 == 1:
        fib = 1
    else:
        fib = prime_fib(n - 1) + prime_fib(n - 2)
    return fib

