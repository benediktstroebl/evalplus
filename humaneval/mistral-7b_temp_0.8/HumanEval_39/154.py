

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
    def fib_gen():
        a, b = 0, 1
        yield a
        yield b
        while True:
            yield a + b
            a, b = b, a + b
    for fib in fib_gen():
        if fib > 1 and fib % fib_gen().__next__() != 0:
            return fib
