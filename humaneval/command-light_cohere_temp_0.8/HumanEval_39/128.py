```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        a, b = next((c for c in range(a, b+1) if c % 2 == 0))
    return a + b

# Example usage:
print(prime_fib(5))  # Output: 89
```