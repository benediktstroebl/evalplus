

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

    primes_table = [0]*2+[2]*(n-1)

    for num in range(2, n+1):
        if primes_table[num] == 0:
            for i in range(2*num, n+1, num):
                primes_table[i] = 1

    return primes_table.index(0, 2*n)

