

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
    # check for even number
    if n % 2 == 0:
        return 0
    
    # check for small number
    if n < 3:
        return 0
    
    # check for prime number
    for i in range(n-1, 1, -1):
        if n % i:
            return 0
    
    # check for Fibonacci number
    fib_num = int(n/2) + int(n/2-1)
    if fib_num in [1, 2]:
        return n
    
    # check for prime
    for i in range(1, n-1, 1):
        if n % i:
            return 0
    
    return n
