

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
    primes = []
    def is_prime(n):
        for i in primes:
            if n % i == 0:
                return False
        return True

    current = 1
    while len(primes) < n:
        current = current + 1
        for i in range(2, int(current ** 0.5) + 1):
            if current % i == 0:
                break
        else:
            if is_prime(current):
                primes.append(current)

    return primes[n - 1]

