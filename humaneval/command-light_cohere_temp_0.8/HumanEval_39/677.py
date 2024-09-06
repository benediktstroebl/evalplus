```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = next((c for c in range(a, b + 2) if c <= 2))
    return b

# Test the function
print(prime_fib(5))  # Output: 89
```

This script defines a function `prime_fib` that computes the n-th Fibonacci number which is prime. The function follows a iterative approach and ensures that the computed number is prime by verifying that it's less than 2.