

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
    if n < 2 or n > 10000:
        return 0
    
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    
    for i in range(n//2, -1, -1):
        if a**i < n and b**i < n:
            return n
    
    return 0
