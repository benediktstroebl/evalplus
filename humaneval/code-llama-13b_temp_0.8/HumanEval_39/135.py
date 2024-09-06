

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
    if n <= 1:
        return n + 1

    m, a, b = n, 1, 1
    while m > 0:
        a, b = b, a + b
        m -= 1

        while b % 2 == 0:
            b = b // 2

        while b % 3 == 0:
            b = b // 3

        while b % 5 == 0:
            b = b // 5

        if a % 2 == 0:
            while a % 2 == 0:
                a = a // 2

        if a % 3 == 0:
            while a % 3 == 0:
                a = a // 3

        if a % 5 == 0:
            while a % 5 == 0:
                a = a // 5

    return a

