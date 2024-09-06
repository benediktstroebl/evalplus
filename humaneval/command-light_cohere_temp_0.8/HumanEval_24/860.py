```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if all(d % k == 0 for k in range(1, n)))) or n)
```