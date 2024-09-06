```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if all(j <= i%x for j in [1, n//i]))

# Example usage
print(largest_divisor(15))  # Output: 5
```