```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not n % d and divisible), -1)
```