

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

    p, q = 1, 2
    while p < n:
        p, q = q, p+q
    
    p = p*p+2*p*(p+1)
    while p % 2 == 0:
        p /= 2

    return p
