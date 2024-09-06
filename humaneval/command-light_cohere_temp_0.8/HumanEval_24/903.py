```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not any(n % d == 0)) + 1)
```
Do you need any further assistance with coding or topic ideas?