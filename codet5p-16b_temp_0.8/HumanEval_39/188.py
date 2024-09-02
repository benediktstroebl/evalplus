

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
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    a, b = 1, 1
    i = 1
    while i!= n:
        c = a + b
        if c % 2 == 0:
            a = b + c
        else:
            a = b
        b = c
        i += 1
    if is_prime(c):
        return c
    return -1

