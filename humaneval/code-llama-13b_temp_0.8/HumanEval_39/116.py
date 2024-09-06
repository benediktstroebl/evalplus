

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
    # Initialization
    a, b, c, counter = 0, 1, 1, 2
    # Loop through the sequence
    while True:
        if is_prime(c) and is_fib(c):
            counter += 1
            if counter == n:
                return c
        a, b, c = b, c, a + b

