

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
    count = 0
    while count < n:
        primes.append(primes[-1] + primes[-2])
        count += 1
        if primes[-2]!= 2 and primes[-2] % 2 == 0:
            primes.pop()
            count -= 1
        if primes[-1] > 1000000:
            return None
    return primes[-1]

