

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
    def is_prime(n: int):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def fib(n: int):
        a = 0
        b = 1
        fib = b
        for _ in range(n - 1):
            a, b = b, a + b
            fib = b
        return fib

    fib_primes = [2]
    i = 2
    while len(fib_primes) < n:
        i += 1
        if is_prime(fib(i)) and is_prime(i):
            fib_primes.append(fib(i))

    return fib_primes[-1]

