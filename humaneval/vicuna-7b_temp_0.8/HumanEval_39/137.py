

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
    if n < 0:
        raise ValueError("n must be a positive integer")
    
    f_n = fibonacci(n)
    is_prime = True
    while True:
        p = prime_pi(f_n)
        if p > f_n:
            break
        if p % f_n == 0:
            is_prime = False
            break
        f_n = p
    return f_n
