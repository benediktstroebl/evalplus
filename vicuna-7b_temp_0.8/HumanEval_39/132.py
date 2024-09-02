

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
    # check if n is prime
    if not n % 2:
        return n + 1
    else:
        if n < 1000000:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return n - i
        for p in primes:
            if n % p == 0:
                return n - p
        return n
