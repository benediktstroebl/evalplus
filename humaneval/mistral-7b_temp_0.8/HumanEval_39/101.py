

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
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    a = 0
    b = 1
    fib = []
    while len(fib) < n:
        c = a + b
        a = b
        b = c
        if is_prime(c):
            fib.append(c)
    return fib[n - 1]

