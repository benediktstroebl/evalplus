

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
    # a and b are the first two numbers of the sequence
    a, b = 0, 1
    for i in range(n):
        # c is the next number of the sequence
        c = a + b
        # a and b are updated
        a, b = b, c
        if is_prime(c):
            return c
