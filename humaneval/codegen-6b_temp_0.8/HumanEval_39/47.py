

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
        raise ValueError("Fibonacci number must be positive")

    fib1 = 1
    fib2 = 1
    count = 3
    while count <= n:
        fib_next = fib1 + fib2
        if is_prime(fib_next):
            fib1 = fib2
            fib2 = fib_next
            count += 1
    return fib_next
