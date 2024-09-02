

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
        return 2

    a = 0
    b = 1
    i = 1
    while True:
        a, b = b, a + b
        if a % 10 == 2 or a % 10 == 3:
            i += 1
        if a == b:
            break
    return i

