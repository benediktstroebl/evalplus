

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
    # Check if n is prime
    if n % 2 != 0 or n % 3 != 0:
        return -1
    
    # Fibonacci sequence starts with 0 and 1, so skip first two numbers
    for i in range(2, n + 1):
        if i == 0 or i == 1:
            continue
        
        # Check if n-i-1 is prime
        if not is_prime(i - 1):
            return -1
        
        # If n-i-1 is prime, then n-i is also prime and it's a Fibonacci number
        # because the difference between consecutive Fibonacci numbers is always prime
        if not is_prime(i):
            return i
        
    return -1
