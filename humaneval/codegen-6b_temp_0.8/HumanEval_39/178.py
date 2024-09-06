

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
    if n < 1:
        raise ValueError("Invalid input")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 2, 3
        for i in range(2, n):
            c = a + b
            b, a = a, c
            while c % 2 == 0:
                c /= 2
            if c == 1:
                return 2*a
        return c

