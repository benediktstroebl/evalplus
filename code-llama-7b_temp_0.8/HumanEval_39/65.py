

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
    a = 0
    b = 1

    if n < 1:
        return None
    elif n == 1:
        return a
    elif n == 2:
        return b

    for i in range(3, n):
        c = a + b
        a = b
        b = c
        if c % 2 != 0:
            for j in range(2, int(c / 2 + 1)):
                if c % j == 0:
                    break
            else:
                return c

    return None

