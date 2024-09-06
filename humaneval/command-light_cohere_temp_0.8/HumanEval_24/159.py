```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if all(j == i%p for j in range(1, n+1)))

# Example usage:
n = 15
result = largest_divisor(n)
print("The largest divisor of", n, "is:", result)
```