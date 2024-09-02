

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
    if n == 1:
        return 2
    elif n == 2:
        return 3

    last = 2
    penult = 3
    num = 5
    while num < n:
        last, penult = penult, last + penult
        while not is_prime(penult):
            penult += last
        num += 1

    return penult
