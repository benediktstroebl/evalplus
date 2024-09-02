

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
    fib = [0, 1]
    a, b = 1, 2
    while True:
        fib.append(a)
        a, b = b, a + b
        for i in fib:
            if i % b == 0:
                return i

