

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
    # fibonacci sequence
    n1 = 0
    n2 = 1
    result = 0
    for i in range(n):
        result = n1 + n2
        n1, n2 = n2, result
    # check primality
    while result % 2 == 0:
        result = result - 1
    return result
