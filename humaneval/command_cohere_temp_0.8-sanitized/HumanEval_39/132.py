from itertools import count
primes = [2, 3]
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for p in primes:
        if n % p == 0:
            return False
    return True
def prime_fib(n):
    if n < 1:
        return None
    it = (x for x in count(start=2) if is_prime(x))
    return next(it) if n == 1 else prime_fib(n - 1) if n == 2 else prime_fib(n - 1) if is_prime(next(it)) else None