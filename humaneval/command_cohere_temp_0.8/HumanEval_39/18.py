Here's a Python script with a self-contained function `prime_fib` that solves the problem:
```python
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
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Initialize first two fibonacci numbers
    a, b = 0, 1
    count = 3

    while count < n:
        # Calculate next fibonacci number
        c = a + b
        a, b = b, c

        # Check if it's a prime
        if is_prime(b):
            count += 1

    return b

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This code defines a function `prime_fib` that generates prime Fibonacci numbers. It optimizes the process by only generating Fibonacci numbers starting from the third Fibonacci number, since the first two are 2 and 3, and both are prime. The code checks primality using a basic primality testing method.