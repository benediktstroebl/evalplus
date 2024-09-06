```python
def largest_divisor(n: int) -> int:
    return next( i for i in range(1, n+1) if any(i % d == 0 for d in range(1, n)))
```
Do you need any assistance with further code related topics?