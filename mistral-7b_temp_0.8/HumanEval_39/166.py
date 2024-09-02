

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
    """
    a = 0
    b = 1
    c = 0
    for x in range(n):
        if x <= 1:
            c = x
            continue
        c = a + b
        if c > n:
            break
        if c % 2 != 0:
            if c != 2:
                for x in range(2, c):
                    if c % x == 0:
                        break
                else:
                    return c
    return c
    """
    """
    a = 1
    b = 2
    for x in range(3, n + 1):
        if x % 2 != 0:
            if x != 3:
                if x > 2:
                    for x in range(2, x):
                        if x % x == 0:
                            break
                    else:
                        return x
    return x
    """
    a = 1
    b = 2
    for x in range(3, n + 1):
        if x
