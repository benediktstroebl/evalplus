

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
    if n <= 0:
        raise ValueError("n should be > 0")

    if n == 1:
        return 2

    primes = [2]
    p = 2

    while True:
        is_prime = True
        for p in primes:
            if p > int(math.sqrt(i)):
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        if len(primes) == n:
            return primes[-1]

