```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if all(d <= x for x in [1, n // d])) or n
```