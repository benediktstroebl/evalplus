```python
from itertools import count, takewhile

def is_prime(n):
    """
    Checks if number is prime
    """
    if n <= 1:
        return False
    for i in count(2):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Initialize two Fibonacci numbers
    a, b = 0, 1
    count = 0

    # Loop to find the nth Fibonacci number that is prime
    while count < n:
        # Check if a is prime
        if is_prime(a):
            count += 1
        # Check if b is prime
        if is_prime(b):
            count += 1
        # Use states to calculate the next Fibonacci numbers
        a, b = b, a + b

    # Return the n-th Fibonacci number that is prime
    return a

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This code defines two functions: `is_prime` checks if a given number is prime, and `prime_fib` returns the n-th Fibonacci number that is also prime. The `prime_fib` function uses a loop to generate the Fibonacci sequence and filters out non-prime numbers using the `is_prime` function. Finally, the function returns the n-th Fibonacci number that is prime.