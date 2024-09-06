```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if all(y % x == 0 for y in range(1, n)))
```