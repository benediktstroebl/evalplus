```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if any(x%y for y in range(1, n)))) or n
```