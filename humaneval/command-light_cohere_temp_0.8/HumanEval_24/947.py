```python
def largest_divisor(n: int) -> int:
    return next( i for i in range(1, n+1) if all(d%i == 0 for d in (1, ..., i, n)))
```