

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
    current = 0
    val = 0
    previous = 1
    fib = 1
    while current < n:
        previous, current = current, previous + fib
        fib = previous + fib
        if is_prime(fib):
            val = fib
            current += 1
    return val

