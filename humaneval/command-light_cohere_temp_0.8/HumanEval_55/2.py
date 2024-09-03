Here's the Python script that includes the Fibonacci function:
```python
def fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Test cases
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
print(fib(0))   # Raises ValueError: n must be a positive integer
```

This code defines the fib function that calculates the n-th Fibonacci number using recursion, and it includes test cases to ensure the function's correctness.  It's a way to solve the problem of calculating Fibonacci numbers in Markdown-like formatting.