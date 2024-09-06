

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
        for i in range(2, n//2):
            if n % i == 0:
                return False
        return True
    f0 = 1
    f1 = 2
    i = 2
    while i < n:
        i += 1
        f2 = (f1 + f0) % 10
        f0 = f1
        f1 = f2
        if is_prime(f2):
            if i == n:
                return f1
            else:
                continue

