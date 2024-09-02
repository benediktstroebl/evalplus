

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

    x, y, count = 1, 1, 1
    while count!= n:
        z = x + y
        x, y = y, z
        if z > 4 * 10**6:
            break
        if z % 2 == 0:
            count += 1
        else:
            count = 1
    return z
