

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

    x = 2
    y = 3
    z = 5
    while z < n:
        z = x + y
        if z % 2!= 0 and z % 3!= 0 and z % 5!= 0:
            z += 1
        else:
            x += 1
            y += 1
    return z

