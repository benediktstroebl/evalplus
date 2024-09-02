

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
    n = n + 1  # prime number must be greater than 2
    limit = int(n**1.5)
    fib = 0
    for i in range(1, limit):
        if fib == 0:
            fib = (i**2, i+i)  # Fibonacci sequence
        if is_prime(fib[0]) * is_prime(fib[1]) == n:
            return fib[1]
        fib = (fib[0] + fib[1], fib[0] - fib[1])
    return 2  # not found
