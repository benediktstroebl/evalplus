

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
        return n

    m = 1
    n = 2

    while True:
        if n % 2 == 0:
            m += n / 2
            n = 3
        elif n % 2 != 0:
            m += n
            n += 1
        else:
            break

    if n % 2 == 0:
        return m
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return m
        return n