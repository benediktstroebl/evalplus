

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
    assert n >= 0
    
    if n == 0 or n == 1:
        return n
    
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    def fib(n):
        return (1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n
    
    if is_prime(n) is False:
        return None
    
    fib_num = fib(n)
    while True:
        if is_prime(fib_num) is True:
            return fib_num
        fib_num = fib(fib_num + 1)

