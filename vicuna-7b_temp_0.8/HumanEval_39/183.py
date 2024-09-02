

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
    # compute n
    n = n - 1
    
    # check if n is prime
    if not is_prime(n):
        return None
    
    # check if n is Fibonacci
    if n <= 2:
        return n
    elif n == 3:
        return 2
    else:
        fib = fibonacci(n-1)
        # prime_fib(fib)
        return fib