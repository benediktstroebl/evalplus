

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
        return -1
    if n == 1:
        return 2

    a = 1
    b = 2
    f = 0
    counter = 2

    while True:
        f = a + b
        a = b
        b = f
        counter += 1
        if is_prime(f) and is_fib(f):
            if counter == n:
                return f

