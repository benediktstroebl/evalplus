

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
        return 1

    fib_1 = 1
    fib_2 = 1
    i = 3
    while i <= n:
        fib_i = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_i
        i += 1

    # check if fib_i is prime
    if is_prime(fib_i):
        return fib_i
    else:
        return None

