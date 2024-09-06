

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

    fib_n = int(n*(3.+1./n))
    if fib_n % 2 == 0:
        return fib_n
    for i in range(3, int(fib_n**.5)+1, 2):
        if fib_n % i == 0:
            return i
    return fib_n
