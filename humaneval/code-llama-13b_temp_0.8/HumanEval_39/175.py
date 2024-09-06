

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
    # find all primes below n
    primes = [2]
    for i in range(3, n, 2):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    # find all Fibonacci numbers below n
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    # return n-th Fibonacci number that is also a prime
    for fib in fibs:
        if fib in primes:
            return fib
