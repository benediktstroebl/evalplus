```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if all(d % x == 0 for x in range(1, n))))
```
Do you require assistance with any other Python programming tasks?