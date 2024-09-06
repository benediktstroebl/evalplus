

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
    # Fibonacci sequence
    a, b = 0, 1
    for i in range(n):
        yield (a, b)
        a, b = b, a + b
    
    # check for primality
    if n <= 2:
        return True
    # find the last prime number
    for p in prime_fib(n - 1):
        if p % n != 0:
            return p
    return True
