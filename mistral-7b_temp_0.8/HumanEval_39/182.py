

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
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    a = 0
    b = 1
    c = 1
    if n > 2:
        for i in range(2, n):
            c = a + b
            if c % 2 == 0:
                a, b = b, c
            else:
                if c > 3:
                    if c % 2 == 0:
                        a, b = b, c
                    else:
                        if c % 3 == 0:
                            a, b = b, c
                        else:
                            for j in range(2, c - 1):
                                if c % j == 0:
                                    a, b = b, c
                                    break
            if b % 2 == 0:
                a, b = b, c

    return b

