Here's a Python script with a self-contained function that solves the problem:
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
    Generates n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Here we could use some optimizations to avoid redundant computations
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    
    # Now we compute the (n-1)-th Fibonacci number which is prime
    result = a + b
    
    while not is_prime(result):
        a, b = b, a + b
        result = a + b
    
    return result
```

The function utilizes two optimizations:
1. For the first few n values, the function directly returns the answer to optimize for time complexity since those values are known.
2. The function "abandons" a Fibonacci number if it is not prime and continues with the next number. This avoids redundant computations and helps with the space complexity.

NOTE: This solution focuses on functionality and correctness, with optimizations being secondary. For a more optimized solution, consider the exponential formula mentioned in the clarifications. 

This script should help you solve the problem and pass corresponding tests. Let me know if it works for you!