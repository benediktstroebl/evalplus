from collections import deque
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    fib = deque([0, 1])
    for _ in range(n - 2):
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
        if is_prime(next_fib):
            return next_fib
    
    return fib[-1]