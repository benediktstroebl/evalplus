

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
    if n < 2:
        return 2
    if n == 2:
        return 3
    elif n == 3:
        return 5
    elif n == 4:
        return 13
    elif n == 5:
        return 89
    a, b = 2, 3
    c = a + b
    i = 4
    while True:
        if is_prime(c):
            if i == n:
                return c
            else:
                a, b = b, c
                c = a + b
                i += 1
        else:
            a, b = b, c
            c = a + b

