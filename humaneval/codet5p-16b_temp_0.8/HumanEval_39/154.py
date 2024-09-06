

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

    def is_prime(n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def fib(n):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def is_fib(n):
        return fib(n) == fib(n - 1) + fib(n - 2)

    def is_fib_prime(n):
        return is_fib(n) and is_prime(fib(n))

    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    else:
        i = 4
        while True:
            if is_fib_prime(i):
                return fib(i)
            i += 1

