

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
    primes = [2]
    fib = [1, 1]
    while fib[len(fib) - 1] < 10**10:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
        prime_to_append = 0
        for p in primes:
            if p * p > fib[len(fib) - 1]:
                break
            if fib[len(fib) - 1] % p == 0:
                prime_to_append = -1
                break
        if prime_to_append != -1:
            primes.append(fib[len(fib) - 1])
            if len(primes) == n:
                return fib[len(fib) - 1]

