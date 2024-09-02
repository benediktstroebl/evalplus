

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
    assert n > 0
    if n == 1:
        return 2
    primes = [2, 3, 5, 7]
    fib = 1
    prime_fibs = [2, 3]
    while len(prime_fibs) < n:
        fib += prime_fibs[-2]
        prime_fibs.append(fib)
        for p in primes:
            if fib % p == 0:
                break
            if p * p > fib:
                primes.append(fib)
                break
    return prime_fibs[-1]
