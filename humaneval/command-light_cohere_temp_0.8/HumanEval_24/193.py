```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))

# Example:
>>> largest_divisor(15)
5
```