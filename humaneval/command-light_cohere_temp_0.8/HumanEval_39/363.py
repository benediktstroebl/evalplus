Here's the corrected code:
```python
import math

def is_prime(n):
    """Return True if n is a prime, False otherwise."""
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

def prime_fibonacci(n):
    """Return the n-th number that is a Fibonacci number and is prime."""
    if n == 0:
        return 0
    if n < 2:
        return 1
    prime = is_prime(n)
    fib = [0]
    fib.append(prime_fibonacci(n - 1))
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib[-1]

# Example usage
print(prime_fibonacci(10))
```

Please let me know if this correctly solves the problem.  I can also assist with any other topic or questions related to Python, coding, algorithms, or math.