### Fibonacci Number Generator
#### Problem Description
The script generates the n-th Fibonacci number, where Fibonacci numbers form a sequence where a number is the addition of the last two numbers, starting with 0 and 1.

#### Solution
Here's a Python function that uses iterative approach to calculate Fibonacci numbers:

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number."""
    
    # Handle edge cases
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    
    # Initialize variables
    a = 1
    b = 1
    
    # Calculate Fibonacci number iteratively
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Test cases
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script first checks for edge cases where `n` is 0 or 1. Then, it initializes variables `a` and `b` to 1, which represents the first two Fibonacci numbers. The Fibonacci number is then calculated iteratively, updating `a` and `b` in each iteration. The final result is returned as `b`.