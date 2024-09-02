

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
        raise ValueError("n must be positive integer")

    a, b = 0, 1
    i = 1
    while i < n:
        a, b = b, a + b
        i += 1

    for c in range(2, a):
        if a % c == 0:
            break
    else:
        return a
    raise ValueError("No such Fibonacci number")

