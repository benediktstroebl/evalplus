

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
    if n == 1 or n == 2:
        return n
    fib_prev, fib = 0, 1
    while True:
        fib_next = fib_prev + fib
        if not is_prime(fib_next):
            fib_prev, fib = fib, fib_next
            continue
        return fib_next

