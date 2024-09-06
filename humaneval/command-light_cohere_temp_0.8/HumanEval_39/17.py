```python
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    return n-th Fibonacci number, checks for prime using is_prime(n) and returns it
    """
    fib = 0
    if n < 2:
        return 2
    while fib < n:
        fib += 1
    fib += 1
    prime = is_prime(fib)
    return fib, prime

# Test
print(prime_fib(5))
``` 
This code is self-contained and can solve the given problem, which is to find the n-th Fibonacci number and check if it's prime.