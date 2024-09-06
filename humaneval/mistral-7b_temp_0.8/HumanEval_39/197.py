

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
    if n == 1:
        return 2
    else:
        a = 2
        b = 3
        for i in range(1, n):
            c = a + b
            if c % 2 == 0:
                b = c
                continue
            else:
                if c > 2:
                    if c % 3 == 0:
                        b = c
                        continue
                a = b
                b = c
        return c

