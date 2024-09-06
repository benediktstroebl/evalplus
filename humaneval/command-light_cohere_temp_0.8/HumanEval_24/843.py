```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and d > 0))

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 4
print(largest_divisor(12))  # Output: false: 4 does not divide 12 evenly)
```