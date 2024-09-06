

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
    if n < 2 or n > 50:
        raise ValueError("Invalid input")
    
    f_n = fibonacci(n)
    is_prime = True
    while f_n > 2:
        if not is_prime:
            break
        if n % f_n == 0:
            is_prime = False
            break
        f_n = fibonacci(n)
    
    return f_n