

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
    a = 1
    b = 1
    count = 1
    while count < n:
        count += 1
        c = a + b
        if c % 2 == 0:
            b = c
        else:
            a = c
            if prime_num(c):
                return c
    return False

