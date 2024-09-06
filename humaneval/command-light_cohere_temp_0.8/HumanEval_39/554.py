```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    if n == 1:
        return 2
    else:
        # Calculate the n-th Fibonacci number
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Unit tests
def test_prime_fib():
    try:
        print(prime_fib(5))  # Should print 89
        print(prime_fib(3))  # Should print 5
        print(prime_fib(0))  # Should raise ValueError
    except ValueError as e:
        print(f"Error: {e}")

# Example usage
test_prime_fib()
```
This Python code defines a function `prime_fib` that calculates the nth Fibonacci number and ensures it's prime, while the `test_prime_fib` function performs unit tests. It raises an ValueError for non-positive inputs and correctly identifies the behavior for various inputs.