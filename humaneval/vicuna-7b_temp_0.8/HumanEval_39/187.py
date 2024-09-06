

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
    # Checking if n is prime
    if not is_prime(n):
        return 0
    
    # Checking if n is greater than 2
    if n < 2:
        return 0
    
    # Calculating fibonacci numbers
    a, b = 0, 1
    n_vals = [a, b]
    for i in range(n - 1):
        n_vals.append(a + b)
    
    # Calculating n-th number
    n_val = n_vals[-1]
    
    # Checking if n is prime
    if not is_prime(n_val):
        return 0
    
    # Checking if n_val is greater than 2
    if n_val < 2:
        return 0
    
    return n_val
