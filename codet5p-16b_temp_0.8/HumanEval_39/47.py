

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
    i = 1
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1
        if (c % 2 == 0):
            continue
        is_prime = True
        for x in range(2, int(c**0.5)+1):
            if c % x == 0:
                is_prime = False
                break
        if is_prime:
            i -= 1
            if i == n:
                return c

