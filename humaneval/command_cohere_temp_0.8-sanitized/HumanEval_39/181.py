def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_fib(n: int):
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # First Fibonacci prime not covered by the bottom n=3 case
        if is_prime(5):
            return 5
        # Filter out even Fibonacci numbers and check primality of the remaining ones
        fib_primes = [x for x in [Fibonacci(i) for i in range(3, n + 1, 2)] if is_prime(x)]
        if not fib_primes:
            return None
        return fib_primes[-1]