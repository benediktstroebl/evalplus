```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if not n % x == 0), 1)
```